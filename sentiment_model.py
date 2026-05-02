def get_sentiment(text):
    text = text.lower()

    negative_words = [
        "sad", "low", "lost", "empty", "tired", "hopeless",
        "worthless", "alone", "burdened", "depressed", "confused"
    ]

    positive_words = [
        "happy", "good", "better", "calm", "hopeful",
        "excited", "great", "amazing", "nice"
    ]

    if any(word in text for word in negative_words):
        return "negative"

    if any(word in text for word in positive_words):
        return "positive"

    return "neutral"