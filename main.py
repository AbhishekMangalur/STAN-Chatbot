from fastapi import FastAPI, Request
from chatbot import generate_response
from memory import recall_user_memory, update_user_memory

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_id = data.get("user_id")
        message = data.get("message")

        if not user_id or not message:
            return {"response": "Missing user_id or message"}

        memory = recall_user_memory(user_id)
        reply, updated_memory = generate_response(message, memory)
        update_user_memory(user_id, updated_memory)

        return {"response": reply}
    except Exception as e:
        print("❌ Server error:", e)
        return {"response": f"Server error: {str(e)}"}
