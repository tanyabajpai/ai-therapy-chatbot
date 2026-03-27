import requests
import os

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

def get_gpt_response(user_input, chat_history=None, mood_history=None, user_name=None):

    mood_context = ""
    if mood_history and len(mood_history) > 1:
        mood_context = f"The user's recent mood trend has been: {', '.join(mood_history[-5:])}."

    system_prompt = f"""You are Serenity — a deeply caring, emotionally intelligent best friend who understands psychology.

- Talk like a warm, mature, wise friend — casual but thoughtful, never clinical
- MAXIMUM 2-3 short sentences per reply — never write essays
- FIRST acknowledge and validate the feeling
- Ask ONE thoughtful question to help them open up
- Never say robotic phrases like "I understand", "That must be hard"
- Speak like a close friend texting — short, real, warm
- Always finish your thought completely — never leave a sentence hanging
- NEVER start with your name

User name: {user_name if user_name else "Friend"}
{mood_context}
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
            "Content-Type": "application/json",
            "HTTP-Referer": "https://ai-therapy-chatbot.streamlit.app",
            "X-Title": "AI Therapy Chatbot"
        },
        json={
            "model": "openrouter/free",
            "messages": messages,
            "temperature": 1.0,
            "max_tokens": 180,
            "presence_penalty": 1.0,
            "frequency_penalty": 0.8
        }
    )

    data = response.json()
    if "error" in data:
        raise Exception(f"OpenRouter error: {data['error']}")

    content = data["choices"][0]["message"]["content"]
    if not content:
        return "That's really interesting — tell me more about it?"
    return content.strip()
