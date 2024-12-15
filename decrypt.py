from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_file(file_path, key):
    """
    Decrypts an AES-256 encrypted file.

    Args:
        file_path (str): Path to the encrypted file.
        key (bytes): AES-256 decryption key (32 bytes).

    Returns:
        None
    """
    try:
        with open(file_path, 'rb') as file:
            iv = file.read(16)  # Read the initialization vector
            encrypted_data = file.read()  # Read the encrypted content

        # Initialize AES cipher
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        # Write the decrypted data to the original file
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

        print(f"File decrypted successfully: {file_path}")
    except Exception as e:
        print(f"Error decrypting file {file_path}: {e}")
