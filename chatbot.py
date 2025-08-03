# import requests
# from utils import detect_tone, ensure_identity, confirm_fact

# OLLAMA_URL = "http://localhost:11434/api/chat"

# def generate_response(message, memory):
#     tone = detect_tone(message)
#     system_prompt = f"You are a helpful assistant. Speak in a {tone} tone."
#     ensure_identity(memory)

#     # ✅ Optional: Check for memory consistency (example for "favorite color")
#     fact_keywords = ["favorite color", "name", "location", "hobby"]
#     for keyword in fact_keywords:
#         contradiction = confirm_fact(memory, keyword, message)
#         if contradiction:
#             reply = contradiction
#             memory.append({"role": "assistant", "content": reply})
#             return reply, memory

#     # Combine memory with new message
#     chat_history = memory + [{"role": "user", "content": message}]
#     payload = {
#         "model": "mistral",  # or "llama3"
#         "messages": [{"role": "system", "content": system_prompt}] + chat_history,
#         "stream": False
#     }

#     try:
#         print("🟡 Sending to Ollama:", payload)
#         response = requests.post(OLLAMA_URL, json=payload)
#         result = response.json()
#         reply = result["message"]["content"].strip()
#         print("✅ Ollama reply:", reply)
#     except Exception as e:
#         return "⚠️ Sorry, I encountered an error processing that.", memory

#     memory.append({"role": "user", "content": message})
#     memory.append({"role": "assistant", "content": reply})
#     return reply, memory


import google.generativeai as genai
from config import GOOGLE_API_KEY
from utils import detect_tone, ensure_identity, confirm_fact

genai.configure(api_key=GOOGLE_API_KEY)

def generate_response(message, memory):
    tone = detect_tone(message)
    system_prompt = f"You are a helpful assistant. Speak in a {tone} tone."
    ensure_identity(memory)

    fact_keywords = ["favorite color", "name", "location", "hobby"]
    for keyword in fact_keywords:
        contradiction = confirm_fact(memory, keyword, message)
        if contradiction:
            reply = contradiction
            memory.append({"role": "assistant", "content": reply})
            return reply, memory

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        chat = model.start_chat(history=[
            {"role": "user" if msg["role"] == "user" else "model", "parts": [msg["content"]]}
            for msg in memory
        ])
        response = chat.send_message(message)
        reply = response.text.strip()
        print("✅ Gemini reply:", reply)

    except Exception as e:
        print("❌ Gemini error:", e)
        return f"⚠️ Sorry, I encountered an error processing that. {e}", memory

    memory.append({"role": "user", "content": message})
    memory.append({"role": "assistant", "content": reply})
    return reply, memory
