import threading
from web_interface import app
from detection import detect_ransomware_behavior
from monitoring import start_monitoring
from encryption import generate_encryption_context
from config import MONITOR_PATH


def main():
    # Initialize homomorphic encryption context
    encryption_context = generate_encryption_context()

    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=lambda: app.run(host="127.0.0.1", port=5000, debug=False), daemon=True)
    flask_thread.start()

    # Start ransomware detection in a separate thread
    detection_thread = threading.Thread(target=detect_ransomware_behavior, daemon=True)
    detection_thread.start()

    # Start monitoring
    start_monitoring(MONITOR_PATH, encryption_context)


if __name__ == "__main__":
    main()
