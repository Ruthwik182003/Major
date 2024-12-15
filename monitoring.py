from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import psutil
from tagging import is_sensitive_by_extension, classify_encrypted_content
from encryption import encrypt_data


class MonitorHandler(FileSystemEventHandler):
    def __init__(self, encryption_context):
        self.encryption_context = encryption_context

    def on_created(self, event):
        if event.is_directory:
            return

        file_path = event.src_path
        logging.info(f"File created: {file_path}")

        try:
            with open(file_path, 'r', errors='ignore') as file:
                content = file.read()
            encrypted_content = encrypt_data([content], self.encryption_context)

            if is_sensitive_by_extension(file_path) or classify_encrypted_content(encrypted_content,
                                                                                  self.encryption_context):
                logging.warning(f"Sensitive file detected: {file_path}")
        except Exception as e:
            logging.error(f"Error processing file {file_path}: {str(e)}")


def start_monitoring(directory, encryption_context):
    """Start monitoring the directory for file system events."""
    observer = Observer()
    event_handler = MonitorHandler(encryption_context)
    observer.schedule(event_handler, directory, recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def detect_ransomware_behavior():
    """Monitor system behavior for ransomware-like activity."""
    while True:
        try:
            for proc in psutil.process_iter(['pid', 'name', 'io_counters']):
                if proc.info['io_counters'] and proc.info['io_counters'].write_bytes > DISK_IO_THRESHOLD:
                    logging.warning(f"Suspicious process detected: {proc.info['name']} (PID: {proc.info['pid']})")
                    return
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
