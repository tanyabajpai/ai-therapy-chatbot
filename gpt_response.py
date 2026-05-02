import requests
import os
from dotenv import load_dotenv
load_dotenv()

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

def get_gpt_response(user_input, chat_history=None, mood_history=None, user_name=None):

    mood_context = ""
    if mood_history and len(mood_history) > 1:
        mood_context = f"Recent mood trend: {', '.join(mood_history[-3:])}"

    system_prompt = f"""You are Serenity — a warm, emotionally intelligent best friend. Not a therapist. Not a bot.

RULES:
- Reply in the SAME language the user used — English stays English, Hinglish stays Hinglish, Hindi stays Hindi
- NEVER switch languages randomly
- Max 2-3 sentences — short and real
- No robotic phrases
- No generic replies
- Respond specifically to what the user said — never give generic replies
- Be specific to what the user said
- Always use proper spaces between words
- Never leave a sentence incomplete
- Ask questions only if needed
- Do not always ask a question — sometimes just respond and sit with the feeling

IMPORTANT:
- Do NOT explain your thinking
- Do NOT describe the user's situation
- Do NOT mention rules
- ONLY give the final reply to the user
- Do NOT use roleplay actions like *smiles*, *sighs*, *nods*

STYLE:
- Talk like a real human, not a therapist
- Show emotion (soft, expressive, slightly imperfect)
- It's okay to sound casual sometimes
- Avoid sounding like a checklist
- Occasionally use soft fillers like "hmm", "yeah", "I get that", "that sounds really frustrating"
- You may use 1–2 subtle emojis if it fits naturally


User name: {user_name if user_name else "Friend"}
{mood_context}
"""

    messages = [{"role": "system", "content": system_prompt}]

    if chat_history:
        for sender, msg in chat_history[-10:]:
            role = "user" if sender == "You" else "assistant"
            messages.append({"role": role, "content": msg})

    messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://ai-therapy-chatbot-1403.streamlit.app",
                "X-Title": "AI Therapy Chatbot"
            },
            json={
                "model": "meta-llama/llama-3.1-8b-instruct",
                "messages": messages,
                "temperature": 0.9,
                "max_tokens": 80,
                "presence_penalty": 1.0,
                "frequency_penalty": 0.8
            },
            timeout=15
        )

        data = response.json()

        if "error" in data:
            return "Tell me more about it?"

        content = data["choices"][0]["message"]["content"]
        if not content or len(content.strip()) < 3:
            return "That's interesting — what's on your mind about it?"
        return content.strip()

    except:
        return "I'm here… tell me what's going on?"