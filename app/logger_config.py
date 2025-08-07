import logging
import sys
from logging.handlers import TimedRotatingFileHandler

def setup_logger():
    """
    Sets up a configured logger that writes to both a file and the console.
    The file handler rotates the log file daily.
    """
    # Get the logger instance
    logger = logging.getLogger("sentim_api_logger")
    logger.setLevel(logging.INFO)

    # Prevent adding duplicate handlers if the function is called multiple times
    if logger.hasHandlers():
        return logger

    # --- File Handler ---
    # Creates a new log file every day and keeps backups
    file_handler = TimedRotatingFileHandler(
        "analysis_log.log", 
        when="midnight", 
        interval=1, 
        backupCount=7, 
        encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)

    # --- Console Handler ---
    # Writes log messages to the console (terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # --- Formatter ---
    # Defines the format of the log messages
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Create and configure the logger instance to be imported by other modules
logger = setup_logger()
