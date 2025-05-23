def get_expert_prompt(code_snippet):
    prompt = f"""You are a senior software engineer with expertise in Python, Java, and JavaScript.  
Provide a concise and accurate summary of the following function, as if explaining to a junior developer.  
Function:  
{code_snippet}
"""
    return prompt
