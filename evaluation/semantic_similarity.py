from sentence_transformers import SentenceTransformer, util
import json

# Load sentence embedding models
bert_model = SentenceTransformer("all-MiniLM-L6-v2")  # BERTScore model

def evaluate_semantic_similarity(reference, generated):
    """Computes BERTScore and USE similarity."""
    
    # Encode sentences
    ref_embedding = bert_model.encode(reference, convert_to_tensor=True)
    gen_embedding = bert_model.encode(generated, convert_to_tensor=True)

    # Compute cosine similarity
    bert_score = util.pytorch_cos_sim(ref_embedding, gen_embedding).item()

    return {
        "BERTScore": round(bert_score, 4),
    }

def evaluate_dataset():
    """Evaluates all summaries in the dataset."""
    with open("gemini_evaluation/java/expert_summaries.json", "r") as file:
        summaries = json.load(file)

    results = []
    for entry in summaries:
        reference = entry.get("reference_summary", "")
        generated = entry["gemini_summary"]  # Can switch to other models

        scores = evaluate_semantic_similarity(reference, generated)
        entry.update(scores)
        results.append(entry)

    with open("gemini_evaluation/java/expert_semantic_similarity_results.json", "w") as file:
        json.dump(results, file, indent=4)

if __name__ == "__main__":
    evaluate_dataset()
    print("Semantic similarity evaluation completed!")
