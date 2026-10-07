import pandas as pd
from openai import OpenAI
import os

client = OpenAI()

df = pd.read_csv("wikipedia_human.csv")
output_file = "ai_dataset.csv"

if os.path.exists(output_file):
    result = pd.read_csv(output_file)
    done = set(result["paragraph_id"])
else:
    result = pd.DataFrame()
    done = set()

for _, row in df.iterrows():
    if row["paragraph_id"] in done:
        continue

    response = client.responses.create(
        model="openai.gpt-oss-120b",
        input=f"""Write an original explanatory passage about the same topic
using only the facts contained in the source.

Do not copy the sentence structure or wording.
Use your own organization and phrasing.
Do not add facts that are not present in the source.
Write naturally and clearly.

Source:
{row["text"]}"""
    )

    new_row = pd.DataFrame([{
        "article_id": row["article_id"],
        "paragraph_id": row["paragraph_id"],
        "human_text": row["text"],
        "ai_text": response.output_text
    }])

    result = pd.concat([result, new_row], ignore_index=True)
    result.to_csv(output_file, index=False)

    print(f"Generated: {len(result)}/{len(df)}")

print("Done!")