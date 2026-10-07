import joblib

model = joblib.load("ai_detector.pkl")

text = input("Enter your text: ")

probabilities = model.predict_proba([text])[0]

human = probabilities[0] * 100
ai = probabilities[1] * 100

print(f"\nAI: {ai:.2f}%")
print(f"Human: {human:.2f}%")

if ai >= 50:
    print("Prediction: AI-generated")
else:
    print("Prediction: Human-written")