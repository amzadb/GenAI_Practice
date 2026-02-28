from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

prompt = input("Enter your prompt: ")
response = client.responses.create(
    model="gpt-5.2",
    input=prompt
)

print(response.output_text)