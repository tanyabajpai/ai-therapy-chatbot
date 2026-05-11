🧠 AI Therapy Chatbot

An emotionally supportive AI chatbot built using Python, Streamlit, NLP, and Large Language Models (LLMs). The system is designed to provide basic emotional support, mood tracking, and crisis detection through real-time conversational interaction.

📌 Project Overview

Mental health issues such as stress, anxiety, loneliness, and emotional burnout have become increasingly common among students and working professionals. Many individuals hesitate to seek help due to social stigma, cost, or limited access to professional support.

This project aims to develop an AI-powered conversational chatbot capable of:

Understanding user emotions
Responding empathetically
Tracking mood over time
Detecting crisis-related inputs
Providing supportive conversation in real time

The chatbot is not intended to replace professional therapists, but instead acts as an accessible emotional support assistant.

🚀 Features

✅ Emotion-Aware Conversations

The chatbot analyzes user messages and detects emotions such as:

Positive
Negative
Neutral

It adapts responses accordingly to maintain empathetic communication.

✅ Crisis Detection System

The application detects harmful or distress-related keywords such as:

“suicide”
“kill myself”
“want to die”
“hurt myself”

If detected, the chatbot immediately displays emergency guidance and helpline support.

✅ Mood Tracking

The chatbot records user mood over multiple interactions and visualizes emotional trends using:

Line graphs
Mood history tables

This helps users observe emotional changes over time.

✅ Voice Input Support

The system also supports voice-based interaction using speech recognition.

✅ Real-Time Chat Interface

Built using Streamlit for a clean and interactive user interface.

🛠️ Technologies Used

Technology	Purpose
Python	Backend Development
Streamlit	Web Interface
NLP	Emotion & Text Processing
OpenRouter API	LLM Response Generation
Pandas	Data Handling
Matplotlib	Mood Visualization
SpeechRecognition	Voice Input
dotenv	API Key Management

📂 Project Structure
AI_Therapy_Chatbot/
│
├── app.py
├── gpt_response.py
├── sentiment_model.py
├── utils.py
├── voice.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
├── models/
├── reports/
└── .streamlit/

⚙️ Installation

1️⃣ Clone Repository
git clone https://github.com/tanyabajpai/ai-therapy-chatbot.git
cd ai-therapy-chatbot

2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
Linux/Mac
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py

The application will open in your browser at:

http://localhost:8501

🧠 Working of the System
Step 1 — User Input

The user enters text or voice input.

Step 2 — Sentiment Analysis

The system checks emotional tone using keyword-based NLP.

Step 3 — Crisis Detection

Sensitive phrases are detected using safety filters.

Step 4 — LLM Response Generation

The chatbot generates emotionally appropriate responses using an LLM API.

Step 5 — Mood Tracking

Mood values are stored and visualized graphically.

📊 Sample Functionalities

Emotional conversation handling
Sentiment-aware replies
Supportive chatbot responses
Crisis alert system
Mood visualization dashboard
Voice-based interaction

📈 Future Improvements

Future enhancements may include:

Advanced emotion detection using deep learning
Multi-language support
Personalized long-term memory
Integration with professional counseling platforms
Voice emotion analysis
Secure cloud deployment

📸 Screenshots

Chat Interface![alt text](<Screenshots/Screenshot 2026-05-03 221853.png>)
Real-time user interaction![alt text](<Screenshots/Screenshot 2026-05-03 225014.png>)
Emotion-aware conversation flow![alt text](<Screenshots/Screenshot 2026-05-03 225014.png>)
Mood Tracking Dashboard![alt text](<Screenshots/Screenshot 2026-05-03 225145.png>)
Mood trend graph![alt text](<Screenshots/Screenshot 2026-05-03 225137.png>)
Emotional history visualization![alt text](<Screenshots/Screenshot 2026-05-03 225145.png>)

🔒 Ethical Considerations

This project focuses on responsible AI practices:

User privacy protection
Safe response generation
Crisis support detection
Transparent AI interaction

The chatbot is designed only for supportive interaction and does not replace professional mental health care.

👩‍💻 Author

Tanya Bajpai

B.Tech CSE Project SRM Institute of Science and Technology

📚 References

Abd-Alrazaq et al., “Mental Health Chatbots,” 2019.
Inkster et al., “Wysa AI,” 2018.
Fitzpatrick et al., “Woebot,” 2017.
Devlin et al., “BERT,” 2019.
Vaswani et al., “Attention is All You Need,” 2017.

⭐ Conclusion

The AI Therapy Chatbot demonstrates how Artificial Intelligence, NLP, and conversational systems can be combined to create accessible emotional support tools. The project successfully integrates sentiment analysis, crisis detection, and mood tracking into a real-time chatbot platform, showcasing the potential of AI-driven mental health assistance systems.