from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from transformers import pipeline

# Use absolute imports from the 'app' package root
from app import crud, schemas
from app.database import get_db
from app.logger_config import logger # Import the configured logger

router = APIRouter(
    prefix="/api/v1",
    tags=["Analysis"],
)

sentiment_analyzer = None
model_loading_error = None

# --- Use the final and validated model ---
MODEL_NAME = "m3hrdadfi/albert-fa-base-v2-sentiment-snappfood"

try:
    logger.info(f"⏳ Loading AI model: '{MODEL_NAME}'...")
    logger.info("Using global Hugging Face login...")
    
    # This model works with the 'sentiment-analysis' pipeline
    sentiment_analyzer = pipeline(
        "sentiment-analysis",
        model=MODEL_NAME,
        use_fast=False # Key fix to prevent tokenizer conversion errors
    )
    logger.info("✅ AI model loaded successfully!")

except Exception as e:
    model_loading_error = e
    logger.error(f"❌ Error loading AI model '{MODEL_NAME}'.")
    logger.error(f"  Error details: {e}")
    logger.warning("⚠️ Server is running, but text analysis will be unavailable.")


def analyze_sentiment_with_ai(text: str) -> schemas.AnalysisResponse:
    # Check if the model was loaded correctly at startup
    if sentiment_analyzer is None:
        error_detail = f"AI model is unavailable due to a startup error. Details: {model_loading_error}"
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=error_detail
        )
    try:
        # This model directly returns a label and a score
        result = sentiment_analyzer(text)
        
        # Log the raw output from the model for debugging purposes
        logger.info(f"Raw model output for text '{text}': {result}")
        
        model_output = result[0]
        label = model_output['label'].lower()
        score = model_output['score']

        # Map the English labels from the model to Persian for the frontend
        sentiment_map = {
            "positive": "مثبت",
            "happy": "مثبت",    # Handle 'happy' as positive
            "negative": "منفی",
            "sad": "منفی",      # Handle 'sad' as negative
        }
        # If the label is not in our map, default to "neutral"
        sentiment = sentiment_map.get(label, "خنثی")

        return schemas.AnalysisResponse(text=text, sentiment=sentiment, score=round(score, 2))
    except Exception as e:
        logger.error(f"An error occurred during text analysis: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred during analysis."
        )

@router.post("/analyze", response_model=schemas.AnalysisResponse)
def analyze_text(
    request: schemas.AnalysisRequest, 
    db: Session = Depends(get_db)
):
    if not request.text.strip():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Text cannot be empty")
    
    analysis_result = analyze_sentiment_with_ai(request.text)
    
    # Save the analysis result to the database
    crud.create_analysis_record(db=db, analysis_data=analysis_result)
    
    return analysis_result
