# OpenAI Quickstart: Simple example of using OpenAI API
# This script demonstrates basic text generation using GPT model
# Requirements: OPENAI_API_KEY environment variable set

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