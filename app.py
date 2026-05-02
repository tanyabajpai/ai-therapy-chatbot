import streamlit as st

st.set_page_config(page_title="AI Therapy Chatbot", page_icon="🧠")
st.title("🧠 AI Therapy Chatbot")

# ---------------- IMPORTS ----------------
try:
    from sentiment_model import get_sentiment  # fallback
    from utils import is_crisis
    from gpt_response import get_gpt_response, get_emotion_score
    from voice import get_voice_input
    import pandas as pd
except Exception as e:
    st.error(f"Import error: {e}")
    st.stop()

# ---------------- SESSION STATE ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "mood_history" not in st.session_state:
    st.session_state.mood_history = []

if "user_name" not in st.session_state:
    st.session_state.user_name = "Tanya"

if "input_key" not in st.session_state:
    st.session_state.input_key = 0

# ---------------- CLEAR CHAT ----------------
if st.button("🗑️ Clear Chat"):
    st.session_state.chat = []
    st.session_state.mood_history = []
    st.rerun()

# ---------------- DISPLAY CHAT ----------------
for sender, msg in st.session_state.chat:
    if sender == "You":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **Bot:** {msg}")

# ---------------- INPUT ----------------
user_input = st.text_input("You:", key=f"input_{st.session_state.input_key}")

col1, col2 = st.columns([1, 5])

with col1:
    send_clicked = st.button("📨 Send")

with col2:
    if st.button("🎤 Speak"):
        voice_text = get_voice_input()
        if voice_text:
            user_input = voice_text

# ---------------- MAIN LOGIC ----------------
if send_clicked and user_input:
    try:
        if is_crisis(user_input):
            response = "⚠️ Please seek immediate help. Contact a trusted person or a mental health helpline right now."
        else:
            # 🔥 GPT-based sentiment with fallback
            try:
                sentiment = get_emotion_score(user_input)
                if sentiment not in ["positive", "neutral", "negative"]:
                    sentiment = get_sentiment(user_input)
            except:
                sentiment = get_sentiment(user_input)

            st.session_state.mood_history.append(sentiment)

            # 🤖 GPT response
            response = get_gpt_response(
                user_input=user_input,
                chat_history=st.session_state.chat,
                mood_history=st.session_state.mood_history,
                user_name=st.session_state.user_name
            )

        # store chat
        st.session_state.chat.append(("You", user_input))
        st.session_state.chat.append(("Bot", response))

        # reset input
        st.session_state.input_key += 1
        st.rerun()

    except Exception as e:
        st.error(f"Error: {e}")

# ---------------- MOOD GRAPH ----------------
if st.session_state.mood_history:
    mood_map = {"positive": 1, "neutral": 0, "negative": -1}

    raw_values = [mood_map.get(m, 0) for m in st.session_state.mood_history]

    # 🔥 Exponential smoothing (better than moving average)
    smoothed = []
    alpha = 0.6

    for i, val in enumerate(raw_values):
        if i == 0:
            smoothed.append(val)
        else:
            smoothed.append(alpha * val + (1 - alpha) * smoothed[-1])

    df = pd.DataFrame({
        "Step": range(1, len(smoothed) + 1),
        "Mood": smoothed
    })

    st.subheader("📊 Emotional Trend (Smoothed)")
    st.line_chart(df.set_index("Step"))