from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
from encryption import encrypt_file
from tagging import is_sensitive_by_extension, classify_file_content

class MonitorHandler(FileSystemEventHandler):
    """Handle file system events."""
    def __init__(self, encryption_key):
        self.encryption_key = encryption_key

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        logging.info(f"File created: {file_path}")

        # Tag and encrypt sensitive files
        if is_sensitive_by_extension(file_path) or classify_file_content(file_path):
            logging.info(f"Sensitive file detected: {file_path}")
            encrypt_file(file_path, self.encryption_key)


def start_monitoring(directory, encryption_key):
    """Start monitoring the directory for file system events."""
    observer = Observer()
    event_handler = MonitorHandler(encryption_key)
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
