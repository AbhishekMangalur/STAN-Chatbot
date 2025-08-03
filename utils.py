def detect_tone(message):
    if any(word in message.lower() for word in ["angry", "frustrated", "hate"]):
        return "calm"
    if any(word in message.lower() for word in ["happy", "excited"]):
        return "cheerful"
    return "neutral"

def ensure_identity(memory):
    for msg in memory:
        if msg["role"] == "user" and "my name is" in msg["content"].lower():
            name = msg["content"].split("is")[-1].strip().split()[0]
            memory.append({
                "role": "system",
                "content": f"Remember this user's name is {name}."
            })
        elif msg["role"] == "user" and "i live in" in msg["content"].lower():
            loc = msg["content"].split("in")[-1].strip().split()[0]
            memory.append({
                "role": "system",
                "content": f"User lives in {loc}."
            })

from memory import get_fact  # make sure to import

def confirm_fact(memory, fact_keyword, new_input):
    past_fact = get_fact(memory, fact_keyword)
    if past_fact and fact_keyword in new_input.lower() and past_fact.lower() not in new_input.lower():
        return f"You mentioned earlier that {past_fact}. Should I update it?"
    return None
