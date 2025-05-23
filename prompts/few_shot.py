def get_few_shot_prompt(code_snippet):
    prompt = f"""Example 1:  
def add(a, b):  
    return a + b  

Summary: This function takes two numbers and returns their sum.  

Example 2:  
def reverse_string(s):  
    return s[::-1]  

Summary: This function returns the reversed version of the input string.  

Now, summarize the following function:  
{code_snippet}
"""
    return prompt
