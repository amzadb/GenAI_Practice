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