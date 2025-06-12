import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
from textblob import TextBlob
from transformers import pipeline
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load emotion classifier from HuggingFace
classifier = pipeline("text-classification", 
                      model="j-hartmann/emotion-english-distilroberta-base", 
                      return_all_scores=True)

positive_emotions = ["joy", "love", "optimism"]
negative_emotions = ["anger", "disgust", "fear", "sadness"]

emotion_suggestions = {
    "joy": ("😊 You're radiating joy!", "Try writing a gratitude journal."),
    "love": ("❤️ Love is in the air!", "Send a kind message to someone."),
    "optimism": ("🌞 Stay hopeful!", "Visualize a positive outcome."),
    "anger": ("😡 Feeling frustrated?", "Try deep breathing or a short break."),
    "disgust": ("🤢 Discomfort noticed.", "Vent in a journal or talk it out."),
    "fear": ("😨 Fear detected.", "Face fears slowly or seek support."),
    "sadness": ("😢 Feeling low?", "Listen to music or talk to a friend.")
}

def analyze_text(text):
    # ✅ Use TextBlob for sentence tokenization (avoids punkt_tab issue in Python 3.13)
    sentences = [str(s) for s in TextBlob(text).sentences]
    summary = {"positive": 0, "negative": 0}
    print("\n📝 Analyzing your sentences...\n")

    for i, sentence in enumerate(sentences, start=1):
        print(f"Sentence {i}: {sentence}")
        
        blob = TextBlob(sentence)
        polarity = blob.sentiment.polarity
        sentiment = "Positive" if polarity > 0 else "Negative"
        summary[sentiment.lower()] += 1
        print(f" - Sentiment: {sentiment} ({polarity:.2f})")

        results = classifier(sentence)[0]
        top_emotion = sorted(results, key=lambda x: x['score'], reverse=True)[0]['label']

        suggestion, tip = emotion_suggestions.get(top_emotion, ("Unknown emotion.", "Try self-care."))
        print(f" - Detected Emotion: {top_emotion}")
        print(f"   💬 {suggestion}")
        print(f"   💡 Suggestion: {tip}\n")

    print("🔚 Summary:")
    print(f" - Positive Sentences: {summary['positive']}")
    print(f" - Negative Sentences: {summary['negative']}")
    print("✨ Keep expressing yourself! 💬")


while True:
    user_input = input("\nEnter your text (or type 'exit' to stop): ")
    if user_input.lower() == 'exit':
        print("Goodbye! Stay emotionally aware 🌈")
        break
    elif user_input.strip() == "":
        print("Please enter a valid sentence.")
    else:
        analyze_text(user_input)
