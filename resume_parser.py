import os
import pdfplumber
from docx import Document

def extract_text(pdf_path):
    ext = os.path.splitext(pdf_path)[1].lower()
    text = ""
    
    # Handle PDF files using pdfplumber
    if ext == '.pdf':
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text()
        return text
        
    # Handle Word files safely
    elif ext == '.docx':
        doc = Document(pdf_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
        
    else:
        return "Unsupported file format."