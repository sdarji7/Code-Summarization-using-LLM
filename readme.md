# 🧠 Exploring the Capabilities of Cohere and Gemini for Source Code Summarization Tasks

This project explores the use of Large Language Models (LLMs) such as **Cohere**, **Gemini** for automated code summarization. We evaluate multiple prompting strategies across Python, JavaScript, and Java using established metrics.

## 📌 Key Features

- 🔍 **Prompt Engineering**: Implements five techniques — Zero-Shot, Few-Shot, Chain-of-Thought, Critique, and Expert.
- 🤖 **Multi-LLM Support**: Compare summaries across Cohere, Gemini, DeepSeek (via Ollama), and LLaMA3 (via Ollama).
- 📊 **Evaluation Metrics**: BLEU, ROUGE-L, METEOR, BERTScore.
- 🧪 **Dataset Coverage**: Experiments span Python, JavaScript, and Java using CodeXGLUE and CodeSearchNet.
- 📑 **IEEE-Style Report**: Comprehensive 6+ page academic report with reproducible experiments.

## 📁 Project Structure
code-summarization/
├── data/ # Dataset download & preprocessing
├── models/ # LLM wrappers (cohere, gemini)
├── prompts/ # Prompt templates & techniques
├── evaluation/ # Metric calculations and statistical tests
├── results/ # Summary outputs and evaluation results
└── main.py # Pipeline entry point

Note: "data" and "raw" can be downloaded from drive link given below
https://drive.google.com/drive/folders/1-ay0g37l1EaxHLRvyPNtmkNlWCG5GuFt?usp=sharing


## 🧪 Evaluation Pipeline

1. **Preprocess datasets** from CodeXGLUE.
2. **Generate summaries** using each LLM with different prompting strategies.
3. **Evaluate quality** using BLEU, ROUGE, METEOR, and BERTScore.
4. **Run statistical tests** (paired t-test, ANOVA) to assess significance.
5. **Export results** to JSON and render in report/visualizations.

## 📊 Prompting Strategies

| Technique       | Description                                           |
|----------------|-------------------------------------------------------|
| Zero-Shot      | Direct summary request without examples               |
| Few-Shot       | Uses labeled examples before actual task              |
| Chain-of-Thought | Encourages step-by-step reasoning                    |
| Critique        | Self-evaluates and refines the summary                |
| Expert          | Simulates senior developer explanation                |

## 📚 Datasets

- Source: [CodeXGLUE](https://github.com/microsoft/CodeXGLUE)
- Languages: Python (251k+), JavaScript (58k+), Java (164k+)
- Preprocessing: Length filtering, deduplication, normalization

📦 Requirements
    Python 3.8+

    Transformers, scikit-learn, scipy, sentence-transformers

    OpenAI & Cohere API keys (Gemini/Cohere access)

📄 Report
    📘 IEEE-style academic paper included in /report, formatted for 2-column publication.
    Includes dataset breakdowns, prompt templates, evaluation results, statistical significance analysis, and limitations.

🤝 Contributor
    Sarthak Darji (202411030) — M.Tech ICT (Software Systems), DA-IICT

