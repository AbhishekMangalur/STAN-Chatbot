from tinydb import TinyDB, Query

db = TinyDB("memory.json")
User = Query()

def recall_user_memory(user_id):
    user_data = db.get(User.user_id == user_id)
    return user_data["memory"] if user_data else []

def update_user_memory(user_id, updated):
    if db.contains(User.user_id == user_id):
        db.update({"memory": updated}, User.user_id == user_id)
    else:
        db.insert({"user_id": user_id, "memory": updated})

def get_fact(memory, keyword):
    keyword = keyword.lower()
    for msg in memory:
        if msg.get("role") == "user" and keyword in msg.get("content", "").lower():
            return msg["content"]
    return None
