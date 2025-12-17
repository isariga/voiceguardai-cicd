from fastapi import FastAPI
from app.model import predict_deepfake

app = FastAPI(title="VoiceGuardAI Inference API")

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/predict")
def predict():
    return predict_deepfake()
