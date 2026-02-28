from dotenv import load_dotenv
load_dotenv()

import anthropic
client = anthropic.Anthropic()

prompt = input("Enter your prompt: ")
message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
)

print(message.content)