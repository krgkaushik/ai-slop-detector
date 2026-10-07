import pandas as pd

df = pd.read_csv("ai_dataset.csv")

for i in range(3):
    print("\n--- HUMAN ---")
    print(df.iloc[i]["human_text"])

    print("\n--- AI ---")
    print(df.iloc[i]["ai_text"])