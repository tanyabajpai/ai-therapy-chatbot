def is_crisis(text):

    crisis_words = ["suicide", "kill myself", "end my life", "die"]

    crisis_words = ["suicide", "kill myself", "end my life", "want to die", "hurt myself"]

    for word in crisis_words:
        if word in text.lower():
            return True
    return False


def detect_emotion_keywords(text):
    text = text.lower()

    if any(word in text for word in ["sad", "empty", "low", "tired"]):
        return "sad"
    if any(word in text for word in ["anxious", "panic", "worried"]):
        return "anxiety"
    if any(word in text for word in ["alone", "lonely"]):
        return "loneliness"

    return None
