from transformers import AlbertTokenizer, AutoModelForSequenceClassification
import os
import logging

# --- Setup basic logging ---
# This will format log messages to include timestamp, level, and the message itself.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# The name of the model we want to download
MODEL_NAME = "m3hrdadfi/albert-fa-base-v2-sentiment-snappfood"
# The name of the directory where the model will be saved
DOWNLOAD_PATH = "sentiment-model-local"

def download_model_final_attempt():
    """
    Downloads and saves the model components using explicit, specific classes.
    This method should bypass any automatic conversion errors.
    """
    # If the model directory already exists, do nothing
    if os.path.exists(DOWNLOAD_PATH) and os.path.isdir(DOWNLOAD_PATH):
        logging.info(f"✅ Model directory '{DOWNLOAD_PATH}' already exists. Skipping download.")
        return

    logging.info(f"⏳ Downloading and saving model: '{MODEL_NAME}'...")
    logging.info("This process only needs to run once and might take a few minutes. Please be patient...")

    try:
        # 1. Download the tokenizer using the specific AlbertTokenizer class
        # This prevents any problematic automatic conversions.
        logging.info(" - Downloading Tokenizer using the specific AlbertTokenizer class...")
        tokenizer = AlbertTokenizer.from_pretrained(MODEL_NAME)
        
        # 2. Download the model itself separately
        logging.info(" - Downloading Model...")
        model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        
        # 3. Save both components to the local directory
        logging.info(f" - Saving files to directory '{DOWNLOAD_PATH}'...")
        tokenizer.save_pretrained(DOWNLOAD_PATH)
        model.save_pretrained(DOWNLOAD_PATH)

        logging.info(f"✅ Model successfully saved in directory '{DOWNLOAD_PATH}'.")
        logging.info("You can now run the main application.")

    except Exception as e:
        logging.error(f"❌ Error while downloading the model: {e}")
        logging.error("Please check your internet connection, the model name, and your Hugging Face token.")

if __name__ == "__main__":
    download_model_final_attempt()
