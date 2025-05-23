import json
from models.cohere_model import summarize_code_cohere
from models.gemini_model import summarize_code_gemini
from models.llama_model import llama3_summarize
from models.deepseek_model import deepseek_summarize

# Import different prompt techniques
from prompts.zero_shot import get_zero_shot_prompt
from prompts.few_shot import get_few_shot_prompt
from prompts.chain_of_thought import get_cot_prompt
from prompts.critique import get_critique_prompt
from prompts.expert import get_expert_prompt

# Load dataset
# with open("data/processed/python_js_java_dataset.json", "r") as file:
#     dataset = json.load(file)

# Load dataset from .jsonl file
dataset = []
with open("data/processed/codexglue_javascript.jsonl", "r") as file:
    for line in file:
        dataset.append(json.loads(line))  # Parse each line as JSON

# Test different prompt techniques, only call one prompt_function incase if using gemini(comment out rest), as gemini has limited quota
prompt_functions = {
    "Zero-Shot": get_zero_shot_prompt,
    "Few-Shot": get_few_shot_prompt,
    "Chain-of-Thought": get_cot_prompt,
    "Critique": get_critique_prompt,
    "Expert": get_expert_prompt,
}

results = []

for item in dataset[:5]:  # Testing on 5 samples
    code_snippet = item["code"]
    reference_summary=item["summary"]

    for prompt_name, prompt_func in prompt_functions.items():
        prompt_text = prompt_func(code_snippet)

        #call one summary model at a time(comment out rest), as calling all together slows down processing
        summary = {
            "function": code_snippet,
            "prompt_type": prompt_name,
            "reference_summary": reference_summary,
            "cohere_summary": summarize_code_cohere(code_snippet, prompt_text),
            "gemini_summary": summarize_code_gemini(code_snippet, prompt_text),
            # "llama3_summary": llama3_summarize(code_snippet, prompt_text),
            # "deepseek_summary": deepseek_summarize(code_snippet, prompt_text),
        }

        results.append(summary)

# Save results
#change .json line to output summaries of different model
with open("results/deepseek_prompting_summaries/javascript_generated/prompting_all.json", "w") as outfile:
    json.dump(results, outfile, indent=4)

print("Prompt Engineering Experiment Completed. Results saved to results folder")
