import psutil
import logging
from config import DISK_IO_THRESHOLD
from alert_system import send_email_alert

def detect_ransomware_behavior():
    """Monitor system behavior for ransomware-like activity."""
    while True:
        try:
            for proc in psutil.process_iter(['pid', 'name', 'io_counters']):
                if proc.info['io_counters'] and proc.info['io_counters'].write_bytes > DISK_IO_THRESHOLD:
                    alert_message = f"Suspicious process detected: {proc.info['name']} (PID: {proc.info['pid']})"
                    logging.warning(alert_message)
                    send_email_alert(alert_message)  # Send alert email
                    return
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
