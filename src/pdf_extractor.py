# src/pdf_extractor.py
import re
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from the given PDF, excluding figure captions
    of the form 'Figure 1: ...'.
    """
    reader = PdfReader(pdf_path)
    full_text = []
    for page in reader.pages:
        page_text = page.extract_text() or ""
        # Remove lines containing "Figure X:"
        cleaned_text = re.sub(r"Figure \d+:[^\n]*", "", page_text)
        full_text.append(cleaned_text)
    return "\n".join(full_text).strip()
