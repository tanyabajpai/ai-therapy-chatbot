# 🧠 AI Therapy Chatbot

An emotionally intelligent AI chatbot that provides supportive conversations, detects user sentiment, and tracks mood patterns over time. Built with a focus on natural, human-like interaction rather than robotic responses.

---

## 🚀 Live Demo

🔗[ [https://ai-therapy-chatbot-1403.streamlit.app](https://ai-therapy-chatbot-1403.streamlit.app/)

---

## 📌 Overview

The **AI Therapy Chatbot** is designed to simulate a supportive conversational companion. It analyzes user input, understands emotional tone, and responds empathetically while maintaining a natural conversational flow.

Unlike typical chatbots, this system focuses on:

* Emotional awareness
* Context retention
* Human-like conversational style

---

## ✨ Features

### 💬 Emotionally Intelligent Conversations

* Detects user sentiment (positive / neutral / negative)
* Generates context-aware, empathetic responses
* Avoids robotic or repetitive replies

### 📊 Mood Tracking

* Tracks user mood over time
* Visualizes emotional trends using interactive charts

### 🧠 Context Awareness

* Maintains recent chat history
* Adapts responses based on conversation flow

### ⚠️ Crisis Detection

* Identifies critical keywords (e.g., self-harm indicators)
* Provides immediate support resources

### 🎤 Voice Input (Extendable)

* Framework ready for speech-based interaction

---

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit
* **Backend:** Python
* **API Integration:** OpenRouter (LLM-based responses)
* **Data Handling:** Pandas
* **Sentiment Analysis:** Rule-based NLP model

---

## 🏗️ Project Structure

```
📦 AI-Therapy-Chatbot
 ┣ 📜 app.py                # Main Streamlit app
 ┣ 📜 gpt_response.py      # LLM response handling
 ┣ 📜 sentiment_model.py   # Sentiment detection logic
 ┣ 📜 utils.py             # Crisis detection + helpers
 ┣ 📜 voice.py             # Voice input module
 ┣ 📜 requirements.txt     # Dependencies
 ┗ 📜 README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-therapy-chatbot.git
cd ai-therapy-chatbot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up API Key

Create a `.env` file (for local development):

```env
OPENROUTER_API_KEY=your_api_key_here
```

OR (for deployment):

* Use Streamlit Secrets to securely store the API key

---

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

| Variable           | Description               |
| ------------------ | ------------------------- |
| OPENROUTER_API_KEY | API key for LLM responses |

---

## 📈 Future Improvements

* Memory-based personalization (long-term user behavior tracking)
* Advanced emotion detection using ML models
* Voice response output (text-to-speech)
* Multi-language emotional adaptation

---

## 🎯 Key Learnings

* Designing human-like conversational AI
* Handling real-world API failures gracefully
* Balancing UX with AI response generation
* Building deployable ML-integrated applications

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is for educational and research purposes.

---

## 👩‍💻 Author

**Tanya Bajpai**

---
