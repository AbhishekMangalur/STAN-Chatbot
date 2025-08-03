# from fastapi import FastAPI, Request
# from chatbot import generate_response
# from memory import recall_user_memory, update_user_memory

# import logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# app = FastAPI()

# @app.post("/chat")
# async def chat(request: Request):
#     try:
#         data = await request.json()
#         user_id = data.get("user_id")
#         message = data.get("message")

#         if not user_id or not message:
#             return {"response": "Missing user_id or message"}

#         memory = recall_user_memory(user_id)
#         reply, updated_memory = generate_response(message, memory)
#         update_user_memory(user_id, updated_memory)

#         return {"response": reply}
#     except Exception as e:
#         print("❌ Server error:", e)
#         return {"response": f"Server error: {str(e)}"}


from fastapi import FastAPI, Request
from chatbot import generate_response
from memory import recall_user_memory, update_user_memory

import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "STAN Chatbot is alive!"}

@app.post("/chat")
async def chat(request: Request):
    try:
        data = await request.json()
        user_id = data.get("user_id")
        message = data.get("message")

        if not user_id or not message:
            logger.warning("Missing user_id or message")
            return {"response": "Missing user_id or message"}

        logger.info(f"📩 Incoming message from {user_id}: {message}")

        memory = recall_user_memory(user_id)
        reply, updated_memory = generate_response(message, memory)
        update_user_memory(user_id, updated_memory)

        logger.info(f"✅ Response to {user_id}: {reply}")
        return {"response": reply}

    except Exception as e:
        logger.error("❌ Server error: %s", str(e))
        return {"response": f"Server error: {str(e)}"}

from fastapi.responses import JSONResponse

@app.get("/")
def root():
return JSONResponse(content={"message": "STAN Chatbot backend is running 🚀"})
