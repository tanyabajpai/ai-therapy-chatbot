def get_sentiment(text):
    text = text.lower()
    positive_words = ["happy", "good", "great", "joy", "love", "excited", "hopeful", "calm", "better", "wonderful", "amazing", "grateful", "fantastic"]
    negative_words = ["sad", "angry", "depressed", "anxious", "hopeless", "empty", "alone", "scared", "worried", "tired", "worthless", "terrible", "awful", "miserable", "pain", "hurt"]
    pos = sum(1 for w in positive_words if w in text)
    neg = sum(1 for w in negative_words if w in text)
    if pos > neg:
        return "positive"
    elif neg > pos:
        return "negative"
    return "neutral"