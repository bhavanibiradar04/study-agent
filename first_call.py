
import os
from dotenv import load_dotenv
from google import genai

# Load the API key from the .env file
load_dotenv()

# Connect to Gemini using the API key
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Show that the request is starting
print("Sending request to Gemini...", flush=True)

# Ask Gemini a question
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Explain RAG in 2 lines for a college student."
)

# Display Gemini's answer
print(response.text)
