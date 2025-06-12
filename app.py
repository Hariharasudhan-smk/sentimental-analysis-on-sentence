from flask import Flask, render_template, request
from textblob import TextBlob
from transformers import pipeline

app = Flask(__name__)

# Load HuggingFace emotion classification model
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    emotion = None
    suggestion = None
    user_input = ""

    if request.method == "POST":
        text = request.form["text"]
        user_input = text

        # Sentiment Analysis
        blob = TextBlob(text)
        sentiment = round(blob.sentiment.polarity, 2)

        # Emotion Analysis
        emotion_result = emotion_classifier(text)
        try:
            emotion = emotion_result[0][0]["label"]
        except (IndexError, KeyError, TypeError):
            emotion = "Unknown"

        # Suggestion
        if sentiment > 0.3:
            suggestion = "Keep up the positive vibes!"
        elif sentiment < -0.3:
            suggestion = "It's okay to have tough days. Stay strong!"
        else:
            suggestion = "Stay neutral and balanced!"

    return render_template("index.html", sentiment=sentiment, emotion=emotion, suggestion=suggestion, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
