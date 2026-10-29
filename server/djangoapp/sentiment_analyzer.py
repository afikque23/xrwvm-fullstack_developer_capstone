from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)


@app.route('/analyze/<text>', methods=['GET'])
def analyze_sentiment(text):
    """Analyze sentiment of the given text."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        sentiment = 'positive'
    elif polarity < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    return jsonify({
        "text": text,
        "sentiment": sentiment,
        "polarity": polarity
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
