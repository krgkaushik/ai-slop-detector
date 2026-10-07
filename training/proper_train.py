
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("ai_dataset.csv")

articles = df["article_id"].unique()

train_articles = articles[:3]
test_articles = articles[3:]

train_df = df[df["article_id"].isin(train_articles)]
test_df = df[df["article_id"].isin(test_articles)]

train_human = pd.DataFrame({
    "text": train_df["human_text"],
    "label": 0
})

train_ai = pd.DataFrame({
    "text": train_df["ai_text"],
    "label": 1
})

test_human = pd.DataFrame({
    "text": test_df["human_text"],
    "label": 0
})

test_ai = pd.DataFrame({
    "text": test_df["ai_text"],
    "label": 1
})

train = pd.concat([train_human, train_ai], ignore_index=True)
test = pd.concat([test_human, test_ai], ignore_index=True)

train = train.sample(frac=1, random_state=42)
test = test.sample(frac=1, random_state=42)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=20000,
        sublinear_tf=True
    )),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(train["text"], train["label"])

pred = model.predict(test["text"])

print("Train articles:", train_articles)
print("Test articles:", test_articles)

print("\nAccuracy:", accuracy_score(test["label"], pred))
print(classification_report(test["label"], pred))

joblib.dump(model, "ai_detector.pkl")

print("Model saved!")