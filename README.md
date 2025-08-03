💬 STAN Chatbot – Human-Like Conversational Agent
STAN is a personalized, context-aware chatbot powered by a local LLM (Mistral or LLaMA3 via Ollama). Built with FastAPI and Streamlit, STAN adapts to user emotions, remembers personal information, and performs intelligent tasks like document summarization — all running locally without API costs.

🚀 Features
Feature	Description
🧠 Human-Like Responses	Generates natural, varied replies (not robotic or templated)
🗣️ Adaptive Tone Matching	Detects emotional tone & adjusts style (happy, angry, neutral, etc.)
📦 Long-Term Memory	Remembers user name, location, interests across sessions (TinyDB)
🔒 Secure API-Free Setup	Runs Mistral/LLaMA3 locally via Ollama — no billing, no tokens
🧾 PDF Summarization	Upload a PDF and STAN will summarize it intelligently
🧠 Identity Recall	Bot remembers facts like “I live in Delhi” or “My favorite color is blue”
🎛 Modular Architecture	Built using FastAPI (backend) and Streamlit (frontend)
📤 Enter-to-Send UI	Press Enter to send message (Shift+Enter for newline)

📂 Project Structure

📁 STAN/
├── app.py                # FastAPI backend (POST /chat)
├── chatbot.py            # Core logic for tone, model, and memory
├── memory.py             # Persistent memory using TinyDB
├── utils.py              # Tone detection and identity handling
├── config.py             # Loads environment variables
├── streamlit_chat.py     # Streamlit-based UI
├── requirements.txt      # Python dependencies
├── memory.json           # Chat memory storage
├── .env                  # For any keys (though not needed with Ollama)
└── README.md             # You're here!

🖥️ Installation

Clone this repo:
git clone https://github.com/yourusername/STAN-chatbot.git

cd STAN-chatbot

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

Install dependencies:
pip install -r requirements.txt

Install Ollama and a model:
Install Ollama → https://ollama.com/download

Then pull a model:
ollama run mistral   # or ollama run llama3

▶️ Running the App
In one terminal, start the FastAPI backend:
uvicorn main:app --reload

In another terminal, start the frontend:
streamlit run streamlit_chat.py

Then visit http://localhost:8501 in your browser.

✅ Test Case Coverage
This project fulfills the full STAN Internship Challenge rubric:

✅ Long-term memory recall

✅ Personalized tone adaptation

✅ Identity consistency under pressure

✅ PDF summarization

✅ No hallucinations or contradictions

✅ Context reuse (e.g., “You said you like anime”)

✅ Natural conversation style (no templates)

📄 Sample Prompts to Try
I live in Bangalore.

My name is Abhishek.

I'm feeling really down today.

What's the summary of this PDF? (Upload a file)

Do you remember where I live?

📘 License
This project is developed for educational purposes and is free to use under the MIT License.