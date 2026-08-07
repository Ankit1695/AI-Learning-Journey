import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key kaha hai bhai?")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

message_user = {
    "role": "user",
    "content": "Give me exactly two unique one-word clothing brand names. Return only the names, one name per line."
}

message_user = {
    "role": "user",
    "content": "Suggest two one-word names for my clothing company."
}

messages = [message_system, message_user]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1
)

print(response)
# print("#######################################")
# print(response.choices[0].message.content)