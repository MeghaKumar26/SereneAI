import json
from datetime import datetime

def log_chat(user_msg, bot_reply, filename="chat_history.json"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "user": user_msg,
        "bot": bot_reply
    }

    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append(entry)

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
