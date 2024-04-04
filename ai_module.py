from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI()


def get_response(sys_prompt: str, message: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": message}
        ]
    )
    return completion.choices[0].message.content
