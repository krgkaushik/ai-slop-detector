import wikipediaapi
import pandas as pd

wiki = wikipediaapi.Wikipedia(
    user_agent="AITextDetector (kaushikgunjkar52gmail.com)",
    language="en"
)

topics = [
    "Artificial intelligence",
    "Machine learning",
    "Computer science",
    "Physics",
    "Biology"
]

data = []

for topic in topics:
    page = wiki.page(topic)

    if page.exists():
        for i, paragraph in enumerate(page.text.split("\n")):
            if len(paragraph.split()) >= 50:
                data.append({
                    "article_id": topic,
                    "paragraph_id": i,
                    "text": paragraph
                })

df = pd.DataFrame(data)

df.to_csv("wikipedia_human.csv", index=False)

print(df.head())
print("Paragraphs:", len(df))