# AI Slop Detector

An NLP-based web application that estimates whether a piece of text is **AI-generated or human-written** using machine learning.

The project uses **TF-IDF** for text feature extraction and **Logistic Regression** for classification. AI-generated training samples are created using **AWS Bedrock GPT-OSS 120B**.

## Features

* Detects AI-generated and human-written text
* Provides AI and human probability scores
* Simple web-based interface
* Fast local predictions
* REST API using FastAPI
* Machine learning model built with Scikit-learn
* AI training data generated using AWS Bedrock

## Tech Stack

* Python
* Scikit-learn
* TF-IDF
* Logistic Regression
* FastAPI
* HTML
* CSS
* JavaScript
* AWS Bedrock
* GPT-OSS 120B

## Project Structure

```text
Ai slop detector/
│
├── app/
│   ├── main.py
│   └── model.py
│
├── models/
│   └── ai_detector.pkl
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── data/
│   ├── ai_dataset.csv
│   ├── train.csv
│   └── wikipedia_human.csv
│
├── training/
│   ├── collect_wikipedia.py
│   ├── generateAi.py
│   ├── train_dataset.py
│   ├── train_model.py
│   └── proper_train.py
│
├── scripts/
│   ├── check.py
│   └── predict.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## How It Works

The detector follows this pipeline:

```text
Human/Wikipedia Text
        ↓
AI Rewriting with AWS Bedrock
        ↓
Labeled Dataset
        ↓
TF-IDF Feature Extraction
        ↓
Logistic Regression
        ↓
Trained Model
        ↓
FastAPI Backend
        ↓
Web Interface
        ↓
AI / Human Probability
```

## Model

The text is converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

The classifier is:

```text
TF-IDF → Logistic Regression
```

The model returns probabilities for both classes:

```text
AI Generated:  72.35%
Human Written: 27.65%
```

The higher probability determines the displayed prediction.

## Dataset

The dataset contains human-written text collected from Wikipedia and AI-generated versions of the same topics.

The current dataset covers topics including:

* Artificial Intelligence
* Machine Learning
* Computer Science
* Physics
* Biology

AI samples were generated using **AWS Bedrock GPT-OSS 120B** while instructing the model to preserve the source facts without copying the original wording or sentence structure.

## Evaluation

The model was evaluated using an **article-level train/test split**, keeping the human and AI versions of the same article together.

Current evaluation:

```text
Accuracy: 89.06%
```

The evaluation is preliminary because the dataset currently contains a small number of source articles.

## Running Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Ai-slop-detector
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_bedrock_api_key
OPENAI_BASE_URL=https://bedrock-mantle.ap-south-1.api.aws/v1
```

Never commit `.env` or expose your API key publicly.

### 5. Start the FastAPI server

```powershell
python -m uvicorn app.main:app --reload
```

### 6. Open the application

Visit:

```text
http://127.0.0.1:8000
```

## API

### POST `/predict`

Request:

```json
{
    "text": "Artificial intelligence is a field of computer science."
}
```

Response:

```json
{
    "ai": 72.35,
    "human": 27.65,
    "prediction": "AI-generated"
}
```

## Limitations

AI-text detection is not perfectly reliable.

The prediction is based on patterns learned from the training dataset and should not be treated as definitive proof that a person or AI wrote a particular piece of text.

The current evaluation dataset is relatively small, so the reported accuracy should be considered an initial result rather than a universal benchmark.

## Future Improvements

* Expand the training dataset
* Add more diverse writing styles
* Test on completely external datasets
* Compare multiple ML algorithms
* Improve robustness against paraphrased AI text
* Add confidence visualization
* Deploy the application online

## Author

**Kaushik Gunjkar**

BE Artificial Intelligence and Data Science

Savitribai Phule Pune University

## License

This project is licensed under the MIT License.

```
```
