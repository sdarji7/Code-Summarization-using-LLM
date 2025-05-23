# models/cohere_model.py

import cohere
import os

COHERE_API_KEY = "qpNXcfMDOtwilysuUuae0bz1Bednzv07XfwFcJfu"

co = cohere.Client(COHERE_API_KEY)

def summarize_code_cohere(code_snippet, prompt_template):
    """Generates a summary using Cohere's API."""
    # prompt = prompt_template.format(code=code_snippet)
    prompt = f"{prompt_template}".replace("{code}", code_snippet)
    response = co.generate(
        model="command-r-plus",
        prompt=prompt,
        max_tokens=500,
        temperature=0.3,
    )
    return response.generations[0].text.strip()

# if __name__ == "__main__":
#     sample_code = "def add(a, b): return a + b"
#     print(summarize_code(sample_code))
