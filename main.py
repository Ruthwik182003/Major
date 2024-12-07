import threading
from flask import Flask
from web_interface import app
from config import MONITOR_PATH, LOG_FILE
from encryption import load_encryption_key, encrypt_file
from tagging import tag_sensitive_files
from detection import detect_ransomware_behavior
from monitoring import start_monitoring
import logging

# Setup Logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def run_flask():
    """Run the Flask web server."""
    app.run(host="127.0.0.1", port=5000, debug=True)

def main():
    # Load or generate encryption key
    encryption_key = load_encryption_key()

    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Start ransomware detection in a separate thread
    detection_thread = threading.Thread(target=detect_ransomware_behavior, daemon=True)
    detection_thread.start()

    # Tag and encrypt existing sensitive files
    sensitive_files = tag_sensitive_files(MONITOR_PATH)
    for sensitive_file in sensitive_files:
        encrypt_file(sensitive_file, encryption_key)

    # Start real-time monitoring
    start_monitoring(MONITOR_PATH, encryption_key)


if __name__ == "__main__":
    main()
