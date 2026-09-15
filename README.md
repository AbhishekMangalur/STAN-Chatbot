# 💬 STAN Chatbot - Intelligent Conversational Agent

Welcome to the STAN Chatbot project! This AI-powered assistant demonstrates human-like interaction, memory, tone awareness, and local+cloud integration. Designed as part of the **STAN Internship Challenge**, this chatbot can be embedded into user-generated content (UGC) platforms and social apps.

---

## 🔥 Features Implemented

| Feature                      | Description                                                            |
| ---------------------------- | ---------------------------------------------------------------------- |
| 💡 Local + Cloud LLM Support | Runs locally with Ollama (Mistral/LLaMA3) or via Gemini Flash 2.5 API  |
| 🧠 Long-Term Memory Recall   | Remembers user identity and preferences with TinyDB                    |
| 🗣️ Tone Adaptation          | Detects tone (happy, sad, angry) and adapts response style dynamically |
| 👥 Personalized Interaction  | Builds context with each conversation to personalize replies           |
| 📄 PDF Summarization         | Upload a PDF and receive a summary via chat                            |
| 📬 Chat UI with Streamlit    | Modern UI with Enter-to-send and chat bubbles                          |
| 📁 Modular FastAPI Backend   | Clean, scalable architecture with memory and chatbot separation        |
| 🔐 Secure Config Management  | .env and config.py for environment settings                            |

---

## 🏗️ Project Structure

```
stan-chatbot/
├── main.py              # FastAPI entry point
├── chatbot.py           # Chat logic (Gemini API or local Ollama)
├── memory.py            # TinyDB-based memory handling
├── utils.py             # Tone detection + identity extraction
├── streamlit_chat.py    # Frontend UI via Streamlit
├── requirements.txt     # Dependencies
├── .env                 # API keys and secrets (excluded via .gitignore)
├── config.py            # Loads environment variables
└── memory.json          # Persistent memory store
```

---

## 🚀 Deployment

This app can be deployed via:

* ✅ Localhost (`uvicorn main:app` + `streamlit run streamlit_chat.py`)
* ☁️ Render (FastAPI backend hosted)
* ⛅ HuggingFace Spaces (Optional for UI)

---

## 📥 Installation (Local)

```bash
git clone https://github.com/your-username/stan-chatbot.git
cd stan-chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt

# Run Backend (Terminal 1)
uvicorn main:app --reload --port 8000

# Run Frontend (Terminal 2)
streamlit run streamlit_chat.py
```

> **Note:** By default, `streamlit_chat.py` connects to `http://127.0.0.1:8000/chat`. You can override this by setting the `BACKEND_URL` environment variable.

---

## ⚙️ Gemini API Setup

1. Get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Add it to your `.env` file:

```env
GOOGLE_API_KEY=your-key-here
```

---

## 🧪 Test Cases (Validated)

* ✅ Long-Term Memory: Remembers name, likes, facts
* ✅ Tone Matching: Detects sadness, humor, emotion
* ✅ Personalization: Remembers interests, adjusts style
* ✅ Naturalness: Varies replies, no template loops
* ✅ Identity Consistency: Doesn’t break character
* ✅ Hallucination Safety: No false claims or memories

---

## 📸 Screenshots

![Diagram](/images/Homepage.png)

![Diagram](/images/reply.png)

&#x20;

---

## 📌 Architecture Overview

* User Input → Streamlit UI → FastAPI Backend
* Gemini API or Ollama → Response → Memory Update
* PDF Summarization → Context-aware Summary

---

## 👨‍💻 Contributors

* Abhishek M (Developer)

---

## 📄 License

This project is licensed for educational use as part of the STAN Internship Challenge.
