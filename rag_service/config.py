import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client=OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# client=OpenAI(
#     api_key="ollama",
#     base_url="http://localhost:11434/v1"
# )

CHAT_MODEL="gemini-2.5-flash-lite"
# CHAT_MODEL="llama3.2:1b"