import nltk
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge
from nltk.translate.meteor_score import meteor_score
import json

nltk.download('wordnet')

def evaluate_text_similarity(reference, generated):
    """Computes BLEU, ROUGE-L, and METEOR scores."""
    rouge = Rouge()

    # Tokenize the input for METEOR
    reference_tokens = reference.split()
    generated_tokens = generated.split()

    bleu_score = sentence_bleu([reference_tokens], generated_tokens)
    meteor = meteor_score([reference_tokens], generated_tokens)  # Fix here
    rouge_scores = rouge.get_scores(generated, reference)[0]

    return {
        "BLEU": round(bleu_score, 4),
        "METEOR": round(meteor, 4),
        "ROUGE-L": round(rouge_scores["rouge-l"]["f"], 4)
    }


def evaluate_dataset():
    """Evaluates all summaries in the dataset."""
    with open("gemini_evaluation/java/expert_summaries.json", "r") as file:
        summaries = json.load(file)

    results = []
    for entry in summaries:
        reference = entry.get("reference_summary", "")
        generated = entry["gemini_summary"]  # Can switch to other models

        scores = evaluate_text_similarity(reference, generated)
        entry.update(scores)
        results.append(entry)

    with open("gemini_evaluation/java/expert_text_similarity_results.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    evaluate_dataset()
    print("Text similarity evaluation completed!")
