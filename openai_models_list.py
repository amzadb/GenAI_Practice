from dotenv import load_dotenv
import os
import openai

load_dotenv()  # Loads variables from .env

api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

models = client.models.list()
for model in models.data:
    print(model.id)
