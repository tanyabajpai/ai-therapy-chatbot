import requests

OPENROUTER_API_KEY = "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"

def get_gpt_response(user_input, chat_history=None, mood_history=None, user_name=None):

    mood_context = ""
    if mood_history and len(mood_history) > 1:
        mood_context = f"User mood trend: {', '.join(mood_history[-5:])}"

    system_prompt = f"""
You are a warm, emotionally intelligent friend — not a therapist, not a chatbot.

Your job is to SUPPORT, not analyze.

STRICT RULES:

1. Keep replies SHORT (max 2 sentences)
2. Speak like a real human texting — natural, simple, warm
3. NEVER overanalyze or combine emotions incorrectly
4. Respond ONLY to what the user JUST said
5. Do NOT assume extra emotions

6. ALWAYS follow this structure:
   - 1st sentence: acknowledge feeling naturally
   - 2nd sentence: gentle question OR supportive statement

7. NEVER say:
   - "I sense..."
   - "It seems like..."
   - "interesting"
   - long explanations

GOOD EXAMPLES:

User: I feel low  
→ "That sounds really heavy... want to share what’s been weighing on you?"

User: I am happy  
→ "That’s really nice to hear 🙂 what made your day better?"

User: I feel lost  
→ "That feeling can be really confusing… what’s been on your mind lately?"

User name: {user_name if user_name else "Friend"}
"""

    messages = [{"role": "system", "content": system_prompt}]

    if chat_history:
        for sender, msg in chat_history[-10:]:
            role = "user" if sender == "You" else "assistant"
            messages.append({"role": role, "content": msg})

    messages.append({"role": "user", "content": user_input})

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/auto",
            "messages": messages,
            "temperature": 1.2,
            "max_tokens": 120,
            "presence_penalty": 1.2,
            "frequency_penalty": 1.0
        }
    )

    data = response.json()

    if "error" in data:
        raise Exception(data["error"])

    return data["choices"][0]["message"]["content"].strip()

def get_emotion_score(user_input):

    prompt = f"""
Classify the emotional tone of this sentence:

"{user_input}"

Return ONLY one:
positive
neutral
negative
"""

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openrouter/auto",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0
        }
    )

    data = response.json()
    return data["choices"][0]["message"]["content"].strip().lower()