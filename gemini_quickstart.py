# Google Gemini Quickstart: Simple example of using Google Gemini API
# This script demonstrates content generation using Gemini Flash model
# Requirements: GOOGLE_API_KEY environment variable set

from dotenv import load_dotenv
load_dotenv()

from google import genai
client = genai.Client()

prompt = input("Enter your prompt: ")
response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents=prompt
)

print(response.text)