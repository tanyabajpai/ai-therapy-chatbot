def get_sentiment(text):
    text = text.lower()

    positive_words = [
        "happy", "good", "better", "calm", "hopeful", "excited",
        "great", "amazing", "nice", "joy", "love", "wonderful",
        "grateful", "khush", "acha", "shopping", "break", "refreshing",
        "relaxed", "enjoying", "fun", "pleased", "smile"
    ]

    negative_words = [
        "sad", "low", "lost", "empty", "tired", "hopeless",
        "worthless", "alone", "burdened", "depressed", "confused",
        "anxious", "scared", "worried", "terrible", "awful",
        "dukhi", "bura", "pareshan", "akela", "stressful", "stress",
        "exhausted", "struggling", "overwhelmed", "not sure", "problem"
    ]

    pos = sum(1 for w in positive_words if w in text)
    neg = sum(1 for w in negative_words if w in text)

    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    return "neutral"