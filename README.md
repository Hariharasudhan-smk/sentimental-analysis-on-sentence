This web application allows users to analyze the **sentiment** and **emotion** of any input text using **Natural Language Processing (NLP)** techniques. It provides a simple and user-friendly interface to understand the emotional tone and polarity of the given text.

🚀 Features

- 📥 Text input form with clean UI
- 📈 Sentiment Analysis using TextBlob (score between -1 and +1)
- 😊 Emotion Detection using HuggingFace's `distilroberta` model
- 💡 Suggestions based on sentiment score
- 🎨 Responsive layout with side-by-side result display
- 🌈 Modern and minimal UI with CSS styling

 🛠 Technologies Used

- 🐍 Python 3
- 🔥 Flask (Web Framework)
- 🧠 TextBlob (Sentiment Analysis)
- 🤗 HuggingFace Transformers (`j-hartmann/emotion-english-distilroberta-base`)
- ⚡ HTML5, CSS3
- 🌐 Bootstrap-style layout (custom CSS, responsive design)

 📂 Folder Structure

sentimental_analysis_web/
│
├── app.py # Main Flask application
├── templates/
│ └── index.html # HTML Template
├── static/
│ └── style.css # CSS Styling
└── README.md # Project Documentation

 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/sentimental_analysis_web.git
   cd sentimental_analysis_web
Install dependencies:
pip install flask textblob transformers torch
Run the app:
python app.py

Open your browser and go to:
http://127.0.0.1:5000/

🧠 Model Info

Sentiment: Uses TextBlob polarity score.
Emotion: Uses HuggingFace distilroberta-base fine-tuned for multi-label emotion classification (joy, sadness, anger, etc.).

🙌 Credits

Developed by Hariharasudhan M
Inspired by applications of AI in emotional intelligence.# sentimental-analysis-on-sentence
This will identify the emotions ,sentiment and give the suggestion to the input suggestion
