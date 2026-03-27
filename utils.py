def is_crisis(text):
    crisis_words = ["suicide", "kill myself", "end my life", "want to die", "hurt myself"]
    for word in crisis_words:
        if word in text.lower():
            return True
    return False
