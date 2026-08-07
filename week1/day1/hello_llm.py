import os
from dotenv import load_dotenv
from groq import Groq

# Load variables from .env file
load_dotenv()

# Read API Key
my_api_key = os.getenv("GROQ_API_KEY")

# Check if API Key exists
if not my_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Create Groq Client
client = Groq(api_key=my_api_key)

# Select Model
model = "llama-3.3-70b-versatile"

# Send Request
response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Do you know test_AI_ankit?"
        }
    ]
)

print(response.choices[0].message.content)
print (answer)