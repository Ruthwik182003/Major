import os

# Monitoring Directory
MONITOR_PATH = "/path/to/monitor"

# Sensitive File Extensions
SENSITIVE_EXTENSIONS = [".docx", ".pdf", ".xlsx", ".txt"]

# ML Model Paths
MODEL_PATH = "ml_classifier_model.pkl"
VECTORIZER_PATH = "tfidf_vectorizer.pkl"

# Encryption Key File
ENCRYPTION_KEY_FILE = "encryption_key.key"

# Logging Configuration
LOG_DIRECTORY = "logs"
LOG_FILE = os.path.join(LOG_DIRECTORY, "system_log.log")

# Flask Configuration
FLASK_HOST = "127.0.0.1"
FLASK_PORT = 5000
DEBUG_MODE = True

# Thresholds
DISK_IO_THRESHOLD = 10**7  # Example threshold for suspicious disk I/O
