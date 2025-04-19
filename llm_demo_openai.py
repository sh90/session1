# pip install openai
from openai import OpenAI

client = OpenAI(api_key="")
response = client.responses.create(
        model="gpt-4o-mini",
        input="I love to eat"
    )
print(response.output_text)
