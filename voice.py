import speech_recognition as sr

def get_voice_input():
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
        return r.recognize_google(audio)
    except Exception:
        return None