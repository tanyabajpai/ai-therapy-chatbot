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

    pos = ["happy","good","great","joy","love","excited","hopeful","calm","better","wonderful","amazing","grateful"]
    neg = ["sad","angry","depressed","anxious","hopeless","empty","alone","scared","worried","tired","worthless","terrible"]
    p = sum(1 for w in pos if w in text)
    n = sum(1 for w in neg if w in text)
    if p > n: return "positive"
    elif n > p: return "negative"
    return "neutral"
