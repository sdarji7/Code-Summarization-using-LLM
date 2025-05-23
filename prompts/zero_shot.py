def get_zero_shot_prompt(code_snippet):
    prompt = f"""Please generate a short comment in one sentence for the following function:{code_snippet}"""
    return prompt
