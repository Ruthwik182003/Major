from cryptography.fernet import Fernet
import os
import logging
from config import ENCRYPTION_KEY_FILE

# Encryption Key Management
def generate_encryption_key():
    """Generate and save an encryption key."""
    key = Fernet.generate_key()
    with open(ENCRYPTION_KEY_FILE, 'wb') as key_file:
        key_file.write(key)
    logging.info("Encryption key generated and saved.")
    return key


def load_encryption_key():
    """Load an encryption key."""
    if not os.path.exists(ENCRYPTION_KEY_FILE):
        return generate_encryption_key()
    with open(ENCRYPTION_KEY_FILE, 'rb') as key_file:
        return key_file.read()


def encrypt_file(file_path, key):
    """Encrypt a file."""
    fernet = Fernet(key)
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = fernet.encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)
        logging.info(f"Encrypted file: {file_path}")
    except Exception as e:
        logging.error(f"Failed to encrypt file: {file_path} - {e}")
