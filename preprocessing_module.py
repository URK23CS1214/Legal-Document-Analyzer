
import re


def preprocess_document(document):

    # Normalize whitespace
    document=re.sub(r"\s+"," ",document)

    # Remove unwanted control characters
    document=re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]","",document)

    return document.strip()
