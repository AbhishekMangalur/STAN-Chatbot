# from tinydb import TinyDB, Query

# db = TinyDB("memory.json")
# User = Query()

# def recall_user_memory(user_id):
#     user_data = db.get(User.user_id == user_id)
#     return user_data["memory"] if user_data else []

# def update_user_memory(user_id, updated):
#     if db.contains(User.user_id == user_id):
#         db.update({"memory": updated}, User.user_id == user_id)
#     else:
#         db.insert({"user_id": user_id, "memory": updated})

# def get_fact(memory, keyword):
#     keyword = keyword.lower()
#     for msg in memory:
#         if msg.get("role") == "user" and keyword in msg.get("content", "").lower():
#             return msg["content"]
#     return None


from tinydb import TinyDB, Query

# Initialize the database
db = TinyDB("memory.json")
User = Query()

# Retrieve a user's memory
def recall_user_memory(user_id):
    user_data = db.get(User.user_id == user_id)
    return user_data["memory"] if user_data else []

# Update a user's memory
def update_user_memory(user_id, updated):
    if db.contains(User.user_id == user_id):
        db.update({"memory": updated}, User.user_id == user_id)
    else:
        db.insert({"user_id": user_id, "memory": updated})

# Get a fact based on a keyword from memory
def get_fact(memory, keyword):
    keyword = keyword.lower()
    for msg in reversed(memory):  # Search from latest to earliest
        if msg.get("role") == "user" and keyword in msg.get("content", "").lower():
            content = msg["content"].lower()
            if " is " in content:
                parts = content.split(" is ")
                if len(parts) > 1:
                    return parts[-1].strip().strip(".!?")
            elif ":" in content:
                parts = content.split(":")
                if len(parts) > 1:
                    return parts[-1].strip().strip(".!?")
            else:
                return msg["content"]
    return None

# Get the last assistant's reply from memory
def get_last_assistant_reply(memory):
    for msg in reversed(memory):
        if msg.get("role") == "assistant":
            return msg.get("content")
    return ""
