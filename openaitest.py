import os
import openai
from config import apikey

openai.api_key = apikey

conversation = [
    {"role": "user", "content": "Hello, Jarvis!"},
    {"role": "assistant", "content": "Hi! How can I assist you today?"}
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

assistant_reply = response['choices'][0]['message']['content']

print(assistant_reply)
