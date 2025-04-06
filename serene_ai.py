import openai
import os
from dotenv import load_dotenv
from chat_logger import log_chat

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_bot_response(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are Serene AI, a calm, friendly mental health assistant. Respond with empathy, warmth, and encouragement. Add helpful emojis where appropriate."},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=150
        )
        reply = response.choices[0].message["content"].strip()
        log_chat(message, reply)
        return reply
    except Exception as e:
        return "Sorry, I'm having a hard time understanding right now. 🌧️ Please try again soon."
