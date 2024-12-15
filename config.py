import os

# Monitoring Directory
MONITOR_PATH = r"D:\\Certifications"

# Sensitive File Extensions
SENSITIVE_EXTENSIONS = [".docx", ".pdf", ".xlsx", ".txt"]

# ML Model Paths
MODEL_PATH = "ml_classifier_model.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

# Logging Configuration
LOG_DIRECTORY = "logs"
LOG_FILE = os.path.join(LOG_DIRECTORY, "system_log.log")

# Flask Configuration
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
DEBUG_MODE = True

# Thresholds
DISK_IO_THRESHOLD = 10**7  # Example threshold for suspicious disk I/O

if not os.path.exists(LOG_DIRECTORY):
    os.makedirs(LOG_DIRECTORY)

# Logging setup
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Capture all levels of logs (DEBUG, INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format for log messages
    handlers=[
        logging.FileHandler(LOG_FILE),  # Save logs to the file
        logging.StreamHandler()  # Also display in the terminal
    ]
)
