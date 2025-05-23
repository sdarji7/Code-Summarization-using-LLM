def get_cot_prompt(code_snippet):
    prompt = f"""Think step by step:

1. First, understand what the function does.  
2. Then, identify the inputs and outputs.  
3. Finally, summarize it clearly.  

Function:  
{code_snippet}"""
    return prompt
