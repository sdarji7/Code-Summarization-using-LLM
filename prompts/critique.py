def get_critique_prompt(code_snippet):
    prompt = f"""Summarize the following function: {code_snippet}  
Now, critique your own summary. Is there anything missing? If yes, refine it.  
"""
    return prompt
