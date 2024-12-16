import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = ""
EMAIL_PASSWORD = ""
EMAIL_RECEIVER = ""


def send_email_alert(message):
    """Send an email alert with the provided message."""
    try:
        # Create email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = "Suspicious Activity Detected"

        # Add message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)

        logging.info("Alert email sent successfully.")
    except Exception as e:
        logging.error(f"Failed to send alert email: {e}")
