import ollama

def llama3_summarize(code_snippet, prompt_template):
    """Generate a code summary using LLaMA3.2 (3B)."""
    
    # prompt = prompt_template.format(code=code_snippet)
    prompt = f"{prompt_template}".replace("{code}", code_snippet)
    response = ollama.chat(model="llama3.2:3b", messages=[{"role": "user", "content": prompt}])
    
    return response["message"]["content"] if "message" in response else "Error: No response."

# Example Usage
if __name__ == "__main__":
    sample_code = "def add(a, b): return a + b"
    prompt = "Summarize this function:\n{code}"
    print(llama3_summarize(sample_code, prompt))

