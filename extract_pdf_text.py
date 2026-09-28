import pdfplumber
import sys

def extract_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        return f"Error reading {pdf_path}: {e}"

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"--- FILE: {path} ---")
        print(extract_text(path))
        print("\n" + "="*50 + "\n")
