# pip install openai
from openai import OpenAI

import data_info

def ask_gpt(prompt):
    client = OpenAI(api_key=data_info.open_ai_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    print(completion.choices[0].message.content)

#
prompt = """
What is 2+2 is
"""
gpt_response = ask_gpt(prompt)
# print("GPT Analysis:", gpt_response)
