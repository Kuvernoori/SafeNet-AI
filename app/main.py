from fastapi import FastAPI, UploadFile, File, Form
from .text_analyzer import analyze_text
from .ocr_analyzer import analyze_image
import tempfile

app = FastAPI(title="SafeNet AI API")

@app.get("/")
def root():
    return {"message": "SafeNet AI API is running"}

@app.post("/analyze_text/") # for text
async def analyze_text_api(text: str = Form(...)):
    result = analyze_text(text)
    return result

@app.post("/analyze_image/") # for image
async def analyze_image_api(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        content = await file.read()
        temp.write(content)
        temp_path = temp.name
    result = analyze_image(temp_path)
    return result
