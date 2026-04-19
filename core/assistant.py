from openai import OpenAI
from config import OPENAI_API_KEY, MODEL
from utils.automation import handle_automation
from core.tts import speak  

client = OpenAI(api_key=OPENAI_API_KEY)

def get_response(user_input):

    # 1. Try automation first
    auto_result = handle_automation(user_input)
    if auto_result:
        speak(auto_result)   # 🔊 speak automation result
        return auto_result

    # 2. AI response
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant. Answer like ChatGPT. Be friendly, short, and clear."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    answer = response.choices[0].message.content

    speak(answer)   # 🔊 speak AI response

    return answer