def get_sentiment(text):
    text = text.lower()
    pos = ["happy","good","great","joy","love","excited","hopeful","calm","better","wonderful","amazing","grateful"]
    neg = ["sad","angry","depressed","anxious","hopeless","empty","alone","scared","worried","tired","worthless","terrible"]
    p = sum(1 for w in pos if w in text)
    n = sum(1 for w in neg if w in text)
    if p > n: return "positive"
    elif n > p: return "negative"
    return "neutral"