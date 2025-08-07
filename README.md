Sentim-API: Intelligent Sentiment AnalyzerA powerful and professional web service (API) based on FastAPI for analyzing the sentiment of Persian texts. This project is designed as a complete portfolio piece to demonstrate mastery of key modern backend development concepts with Python, including database interaction, migration management, and AI model integration.✨ Key FeaturesSentiment Analysis API: Receives text and returns its sentiment (positive, negative, or neutral).Asynchronous: Fully utilizes async and await for maximum performance.Database: Uses SQLAlchemy to interact with a SQLite database and store analysis history.Database Migrations with Alembic: For professionally creating and updating the database schema.Pydantic Models: For validating input (Request Body) and output (Response Model) data.Modular Routing: Organizes endpoints into separate modules (analysis, pages, history).Web Interface: A simple web page using Jinja2 Templates to test the API, and view and delete history.Lifespan Events: Manages startup and shutdown processes.Middleware: Adds an X-Process-Time header to all responses for monitoring processing time.Advanced Logging: Logs all events and errors to both the console and a separate file (analysis_log.log) with daily rotation.Environment Variable Management: Uses a .env file to securely manage tokens and sensitive information.🛠️ Technologies UsedFastAPI: The core web frameworkUvicorn: The ASGI server for running the applicationSQLAlchemy: For database interaction (ORM)Alembic: For managing database schema changes (Migrations)Pydantic: For data validationJinja2: The template engine for rendering HTMLTransformers (Hugging Face): For loading and using AI modelsPython-dotenv: For managing environment variables🧠 About the AI ModelThis project uses the m3hrdadfi/albert-fa-base-v2-sentiment-snappfood model for sentiment analysis.Architecture: This model is based on the ALBERT (A Lite BERT) architecture, which is an optimized and lighter version of the famous BERT model. This feature allows the model to be faster and have a smaller footprint while maintaining high accuracy.Training Data: The model was specifically trained on a dataset of user reviews from Snappfood (a popular Iranian food delivery app). This has given the model an excellent understanding of colloquial language, everyday slang, and the tone of Persian-speaking users online.Strengths: Due to its training on real-world reviews, it is very powerful in detecting sentiment in informal and short texts.Potential Limitations: Since the training data is primarily focused on food and restaurant reviews, it may face challenges when analyzing highly specialized texts (such as scientific or literary documents).In this project, we use the model in an offline mode. A separate script (download_model.py) is responsible for downloading and saving the model to a local directory, and the main application loads the model from the disk. This approach significantly increases the application's stability and startup speed.🏗️ Project Structuresentim-api/
├── .env                      # Environment variables file (for token)
├── alembic/                  # Alembic configuration folder
├── app/                      # Main application source code
│   ├── __init__.py
│   ├── crud.py               # Database operations functions (CRUD)
│   ├── database.py           # Database connection settings
│   ├── logger_config.py      # Advanced logging configuration
│   ├── main.py               # FastAPI application entry point
│   ├── models.py             # SQLAlchemy ORM models
│   ├── schemas.py            # Pydantic models
│   ├── routers/              # Router modules
│   │   ├── analysis.py       # Text analysis endpoints
│   │   ├── history.py        # History deletion endpoints
│   │   └── pages.py          # Web page endpoints
│   └── templates/            # HTML templates (Jinja2)
│       └── index.html
        └── base.html
├── alembic.ini               # Alembic config file
├── analysis_log.log          # Log output file
├── download_model.py         # Offline model download script
├── README.md                 # This file
├── .gitignore
└── requirements.txt          # List of required libraries
🚀 Setup and ExecutionPrerequisite: Python 3.9 or higherClone the project:git clone <YOUR-GITHUB-PROJECT-URL>
cd sentim-api
Create and activate a virtual environment:# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install the required libraries:pip install -r requirements.txt
Set up the Hugging Face token:Create a file named .env in the project root.Copy your access token from the Hugging Face website and place it in the file as follows:HF_TOKEN="hf_...your_token_here..."
Download the model offline (only once): Run the following script to download and save the model locally.python download_model.py
Create the database with Alembic: This command creates the initial version of the tables in the database.alembic upgrade head
Run the server:uvicorn app.main:app --reload
The server will be running at http://127.0.0.1:8000.🔌 API DocumentationAfter running the server, visit http://127.0.0.1:8000/docs to view the interactive Swagger documentation.