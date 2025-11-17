import pytesseract
from PIL import Image
from .text_analyzer import analyze_text

def analyze_image(image_path: str):
    text = pytesseract.image_to_string(Image.open(image_path))
    text_result = analyze_text(text)
    return {
        "ocr_text": text, # we calculate initials thgrow ocr text so we can extract 
        "label": text_result["label"],
        "score": text_result["score"]
    }
