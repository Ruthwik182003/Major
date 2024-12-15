import os
import logging
import pickle
from config import SENSITIVE_EXTENSIONS, MODEL_PATH, VECTORIZER_PATH
from encryption import decrypt_data
def is_sensitive_by_extension(file_name):
    """Check if a file is sensitive based on its extension."""
    _, ext = os.path.splitext(file_name)
    return ext in SENSITIVE_EXTENSIONS

def classify_encrypted_content(encrypted_content, context):
    """Classify file content using a pre-trained ML model."""
    decrypted_data = decrypt_data(encrypted_content)
    with open(MODEL_PATH, 'rb') as model_file:
        classifier = pickle.load(model_file)
    with open(VECTORIZER_PATH, 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    transformed_data = vectorizer.transform([decrypted_data])
    return classifier.predict(transformed_data)[0]