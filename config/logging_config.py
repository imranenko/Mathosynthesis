import logging
from config.config import LOG_LEVEL, LOG_FILE_PATH

def setup_logging():
    # Get the root logger instance and set logging level based on config
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, LOG_LEVEL))

    # Create file handler to write logs to a file
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setLevel(logging.INFO)

    # Create console handler to output logs to the console and set logging level basen on config
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL))

    # Define the log message format (timestamp, logger name, level, and message)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    

    # Apply the formatter to both file and console handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add file and console handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)