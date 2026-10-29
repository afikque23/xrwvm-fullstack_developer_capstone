import requests
import json
import os
import logging

logger = logging.getLogger(__name__)

backend_url = "http://localhost:3030"
sentiment_analyzer_url = "http://localhost:5000"

# Local data fallback
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "database", "backend", "data.json")

# In-memory storage for reviews added via API
_reviews_added = []

# Simple positive/negative word lists for sentiment analysis
POSITIVE_WORDS = {
    'great', 'good', 'excellent', 'amazing', 'wonderful', 'fantastic',
    'outstanding', 'superb', 'brilliant', 'perfect', 'best', 'awesome',
    'happy', 'love', 'satisfied', 'recommend', 'helpful', 'friendly',
    'nice', 'pleasant', 'impressive', 'exceptional', 'superior', 'terrific'
}
NEGATIVE_WORDS = {
    'bad', 'poor', 'terrible', 'awful', 'horrible', 'worst', 'disappointing',
    'disappointed', 'unsatisfied', 'unhappy', 'hate', 'dislike', 'rude',
    'unhelpful', 'slow', 'broken', 'problem', 'issue', 'fail', 'failed',
    'waste', 'overpriced', 'scam', 'dishonest', 'fraud'
}


def _load_local_data():
    """Load dealership and review data from local JSON file."""
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading local data: {e}")
        return {"dealerships": [], "reviews": []}


def get_request(endpoint, **kwargs):
    """Try backend URL first, fall back to local data."""
    try:
        request_url = f"{backend_url}{endpoint}"
        response = requests.get(request_url, timeout=2)
        return response.json()
    except Exception:
        # Fall back to local data
        return _local_get_request(endpoint, **kwargs)


def _local_get_request(endpoint, **kwargs):
    """Serve data from local JSON file."""
    data = _load_local_data()
    dealerships = data.get("dealerships", [])
    reviews = data.get("reviews", []) + _reviews_added

    if endpoint == "/fetchDealers":
        return dealerships
    elif endpoint.startswith("/fetchDealers/"):
        state = endpoint.split("/fetchDealers/")[1]
        return [d for d in dealerships if d.get("state", "").lower() == state.lower()
                or d.get("st", "").lower() == state.lower()]
    elif endpoint.startswith("/fetchDealer/"):
        dealer_id = int(endpoint.split("/fetchDealer/")[1])
        result = [d for d in dealerships if d.get("id") == dealer_id]
        return result
    elif endpoint.startswith("/fetchReviews/dealer/"):
        dealer_id = int(endpoint.split("/fetchReviews/dealer/")[1])
        return [r for r in reviews if r.get("dealership") == dealer_id]
    return []


def _simple_sentiment(text):
    """Simple keyword-based sentiment analysis."""
    words = text.lower().split()
    positive_count = sum(1 for w in words if w in POSITIVE_WORDS)
    negative_count = sum(1 for w in words if w in NEGATIVE_WORDS)
    
    if positive_count > negative_count:
        return {"sentiment": "positive", "polarity": 0.5}
    elif negative_count > positive_count:
        return {"sentiment": "negative", "polarity": -0.5}
    else:
        return {"sentiment": "neutral", "polarity": 0.0}


def analyze_review_sentiments(text):
    """Analyze sentiment - try external service first, fall back to keyword analysis."""
    try:
        response = requests.get(f"{sentiment_analyzer_url}/analyze/{text}", timeout=2)
        return response.json()
    except Exception:
        return _simple_sentiment(text)


def post_review(data_dict):
    """Try backend first, fall back to local storage."""
    try:
        response = requests.post(f"{backend_url}/insert_review", json=data_dict, timeout=2)
        return response.json()
    except Exception:
        # Store locally
        review = {"id": len(_reviews_added) + 100, **data_dict}
        _reviews_added.append(review)
        return {"status": 200, "message": "Review added"}
