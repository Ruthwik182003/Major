import os
import logging
import pickle
from config import SENSITIVE_EXTENSIONS, MODEL_PATH, VECTORIZER_PATH

def is_sensitive_by_extension(file_name):
    """Check if a file is sensitive based on its extension."""
    _, ext = os.path.splitext(file_name)
    return ext in SENSITIVE_EXTENSIONS


def classify_file_content(file_path):
    """Classify file content using a pre-trained ML model."""
    try:
        with open(file_path, 'r', errors='ignore') as file:
            content = file.read()

        # Load pre-trained model and vectorizer
        with open(MODEL_PATH, 'rb') as model_file:
            classifier = pickle.load(model_file)

        with open(VECTORIZER_PATH, 'rb') as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)

        # Transform the content and classify
        transformed_content = vectorizer.transform([content])
        return classifier.predict(transformed_content)[0]
    except Exception as e:
        logging.error(f"Error classifying file content: {file_path} - {e}")
        return False


def tag_sensitive_files(directory):
    """Tag sensitive files in the specified directory."""
    sensitive_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            if is_sensitive_by_extension(file) or classify_file_content(file_path):
                logging.info(f"Sensitive file tagged: {file_path}")
                sensitive_files.append(file_path)

    return sensitive_files
