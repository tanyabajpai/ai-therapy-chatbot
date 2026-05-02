def is_crisis(text):
<<<<<<< HEAD
    crisis_words = ["suicide", "kill myself", "end my life", "die"]
=======
    crisis_words = ["suicide", "kill myself", "end my life", "want to die", "hurt myself"]
>>>>>>> 15c09b086265103bf3e2fa842e290f13a4df3506
    for word in crisis_words:
        if word in text.lower():
            return True
    return False
<<<<<<< HEAD

def detect_emotion_keywords(text):
    text = text.lower()

    if any(word in text for word in ["sad", "empty", "low", "tired"]):
        return "sad"
    if any(word in text for word in ["anxious", "panic", "worried"]):
        return "anxiety"
    if any(word in text for word in ["alone", "lonely"]):
        return "loneliness"

    return None
=======
>>>>>>> 15c09b086265103bf3e2fa842e290f13a4df3506
