import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file containing GEMINI_API_KEY
load_dotenv(dotenv_path="venv/.env")
api_key = os.getenv("gemini-api-key")
genai.configure(api_key=api_key)

# Initialize Gemini model (use gemini-1.5-flash or gemini-2.0 if available)
model = genai.GenerativeModel("gemini-2.0-flash")

chat_history = []  # list of (user, bot) pairs

def build_prompt(history, user_input):
    prompt = (
        "You are a friendly and polite assistant. Always be helpful, positive, and easy to understand.\n"
    )
    for user, bot in history[-3:]:
        prompt += f"User: {user}\nAssistant: {bot}\n"
    prompt += f"User: {user_input}\nAssistant:"
    return prompt

def chat_with_model(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Error:", str(e))
        return "Sorry, something went wrong."

print("🤖 Gemini Flash Chatbot. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    prompt = build_prompt(chat_history, user_input)
    bot_response = chat_with_model(prompt)
    print("🤖", bot_response)

    chat_history.append((user_input, bot_response))
