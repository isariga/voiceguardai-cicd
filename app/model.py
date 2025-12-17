import random

def predict_deepfake():
    label = random.choice(["REAL", "FAKE"])
    confidence = round(random.uniform(0.6, 0.99), 2)

    return {
        "label": label,
        "confidence": confidence
    }
