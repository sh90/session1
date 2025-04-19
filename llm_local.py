# pip install transformers torch
# pip install accelerate

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Choose a model from Hugging Face
model_name = "gpt2"

# Download and load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Your input prompt
prompt = "Explain black holes in simple terms."

# Tokenize input
inputs = tokenizer(prompt, return_tensors="pt")

# Generate a response
output = model.generate(**inputs, max_length=100, do_sample=True, temperature=0.7)

# Decode and print the response
response_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(response_text)
