import pandas as pd

df = pd.read_csv("ai_dataset.csv")

human = pd.DataFrame({
    "text": df["human_text"],
    "label": 0
})

ai = pd.DataFrame({
    "text": df["ai_text"],
    "label": 1
})

dataset = pd.concat([human, ai], ignore_index=True)
dataset = dataset.sample(frac=1, random_state=42)

dataset.to_csv("train.csv", index=False)

print(dataset.head())
print("Total:", len(dataset))
print(dataset["label"].value_counts())