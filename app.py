import streamlit as st

st.set_page_config(page_title="AI Therapy Chatbot", page_icon="🧠")
st.title("🧠 AI Therapy Chatbot")

try:
    from sentiment_model import get_sentiment
    from utils import is_crisis
    from gpt_response import get_gpt_response
    from voice import get_voice_input
    import pandas as pd
except Exception as e:
    st.error(f"Import error: {e}")
    st.stop()

if "chat" not in st.session_state:
    st.session_state.chat = []
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []
if "user_name" not in st.session_state:
    st.session_state.user_name = "Tanya"
if "input_key" not in st.session_state:
    st.session_state.input_key = 0

if st.button("🗑️ Clear Chat"):
    st.session_state.chat = []
    st.session_state.mood_history = []
    st.rerun()

for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")

user_input = st.text_input("You:", key=f"input_{st.session_state.input_key}")

col1, col2 = st.columns([1, 5])
with col1:
    send_clicked = st.button("📨 Send")
with col2:
    if st.button("🎤 Speak"):
        voice_text = get_voice_input()
        if voice_text:
            user_input = voice_text

if send_clicked and user_input:
    try:
        if is_crisis(user_input):
            response = "⚠️ Please seek immediate help. Call iCall: 9152987821"
        else:
            sentiment = get_sentiment(user_input)
            st.session_state.mood_history.append(sentiment)

            # ✅ ADD THIS BLOCK HERE
            emotion_map = {
                "negative": "I'm really sorry you're feeling this way. ",
                "positive": "That actually sounds really nice. ",
                "neutral": ""
            }

            emotion_prefix = emotion_map.get(sentiment, "")

            # ✅ MODIFY THIS LINE
            response = get_gpt_response(
                user_input=emotion_prefix + user_input,
                chat_history=st.session_state.chat,
                mood_history=st.session_state.mood_history,
                user_name=st.session_state.user_name
            )
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))
        st.session_state.input_key += 1
        st.rerun()
    except Exception as e:
        st.error(f"Error: {e}")

if st.session_state.mood_history:
    mood_map = {"positive": 1, "neutral": 0, "negative": -1}
    mood_values = [mood_map[m] for m in st.session_state.mood_history]
    df = pd.DataFrame({
        "Message": range(1, len(mood_values) + 1),
        "Mood": mood_values
    })
    st.subheader("📊 Mood Tracking Over Time")
    st.line_chart(df.set_index("Message"))