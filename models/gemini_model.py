# models/gemini_model.py

import google.generativeai as genai
import os

GEMINI_API_KEY = "AIzaSyBl7aKv3LrBq9xsUmRV3Rjka5xzLozgtxA"

genai.configure(api_key=GEMINI_API_KEY)

def summarize_code_gemini(code_snippet, prompt_template):
    """Generates a summary using Google's Gemini API."""
    # prompt = prompt_template.format(code=code_snippet)
    prompt = f"{prompt_template}".replace("{code}", code_snippet)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# if __name__ == "__main__":
#     sample_code = "def multiply(a, b): return a * b"
#     print(summarize_code(sample_code))
