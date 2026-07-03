"""
-------------------------------------------------------
PDF Utilities
-------------------------------------------------------
"""

import fitz


def extract_text_from_pdf(filepath: str) -> str:
    """
    Extract all text from a PDF file.
    """

    document = fitz.open(filepath)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text.strip()