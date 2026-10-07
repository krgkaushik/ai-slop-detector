import joblib

model = joblib.load("models/ai_detector.pkl")

def predict_text(text):
    probabilities = model.predict_proba([text])[0]

    human = probabilities[0] * 100
    ai = probabilities[1] * 100

    return {
        "ai": round(ai, 2),
        "human": round(human, 2),
        "prediction": "AI-generated" if ai >= 50 else "Human-written"
    }