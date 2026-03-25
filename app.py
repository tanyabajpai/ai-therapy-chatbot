import streamlit as st
from sentiment_model import get_sentiment
from utils import is_crisis
import pandas as pd
from gpt_response import get_gpt_response
from voice import get_voice_input

st.set_page_config(page_title="AI Therapy Chatbot", page_icon="🧠")
st.title("🧠 AI Therapy Chatbot")

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

# Display chat history
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")

# Input box with dynamic key so it clears after each send
user_input = st.text_input("You:", key=f"input_{st.session_state.input_key}")

col1, col2 = st.columns([1, 5])

with col1:
    send_clicked = st.button("📨 Send")

with col2:
    if st.button("🎤 Speak"):
        voice_text = get_voice_input()
        if voice_text:
            user_input = voice_text
            st.write(f"You (voice): {voice_text}")

if send_clicked and user_input:
    try:
        if is_crisis(user_input):
            response = "⚠️ Please seek immediate help. Contact a trusted person or a mental health helpline right now."
        else:
            sentiment = get_sentiment(user_input)
            st.session_state.mood_history.append(sentiment)

            response = get_gpt_response(
                user_input=user_input,
                chat_history=st.session_state.chat,
                mood_history=st.session_state.mood_history,
                user_name=st.session_state.user_name
            )

        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

        # This clears the input box
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