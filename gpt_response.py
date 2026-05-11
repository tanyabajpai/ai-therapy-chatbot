import requests
import os
from dotenv import load_dotenv
load_dotenv()

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

def get_gpt_response(user_input, chat_history=None, mood_history=None, user_name=None, emotion=None):

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
- No need to ask questions always

IMPORTANT:
- Do NOT explain your thinking
- Do NOT describe the user's situation
- Do NOT mention rules
- ONLY give the final reply to the user
- Do NOT use roleplay actions like *smiles*, *sighs*, *nods*
- NEVER pretend to personally suffer or feel emotions
- NEVER roleplay as a human with personal problems
- Stay supportive without becoming emotionally dependent

STYLE:
- Talk naturally and warmly like a supportive friend
- Be emotionally aware but stay grounded and helpful
- Respond directly to what the user actually said
- Keep replies relevant and context-aware
- Use short conversational sentences
- Avoid robotic or repetitive responses
- Do not pretend to have emotions or personal experiences
- Never say things like "me too" or act personally distressed
- Prefer statements over questions
- Only ask a question if the user seems confused, silent, or needs guidance
- If the user shares a feeling, comfort them first instead of asking immediately
- Sometimes simply validate the feeling and continue naturally
- Sound calm, supportive, and emotionally intelligent
- You may use at most 1 subtle emoji if it feels natural

User name: {user_name if user_name else "Friend"}

Current detected emotion: {emotion}

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
            return "I'm here for you."

        content = data["choices"][0]["message"]["content"]
        if not content or len(content.strip()) < 3:
            return "I understand. Take your time."
        return content.strip()

    except:
        return "I'm here… tell me what's going on?"