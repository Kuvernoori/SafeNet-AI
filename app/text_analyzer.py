from transformers import pipeline


nlp_model = pipeline("text-classification", model="unitary/toxic-bert", truncation=True)

def analyze_text(text: str):
    if not text:
        return {"label": "neutral", "score": 0.0} # special labels like toxic or not
    result = nlp_model(text)[0]
    label = "toxic" if "toxic" in result["label"].lower() else "neutral"
    return {"label": label, "score": round(result["score"], 3)}
