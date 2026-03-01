# Anthropic Claude Quickstart: Simple example of using Anthropic API
# This script demonstrates message-based interaction with Claude model
# Requirements: ANTHROPIC_API_KEY environment variable set

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