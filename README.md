# ⚖️ Automated Legal Document Analyzer

An AI-powered application that analyzes legal documents, summarizes important information, and identifies key clauses using Python, Streamlit, and a locally hosted LLM through Ollama.

> **Note:** This project uses Llama 3.2 locally through Ollama as a free alternative to the GPT-4 model specified in the original lab experiment.

## Features

- Enter legal text directly or upload a TXT/PDF document
- Preprocess and normalize document text
- Extract parties, purpose, obligations, payment terms, duration, and termination conditions
- Identify important dates and legal clauses
- Generate a structured legal document summary
- Save the analysis report as a text file
- Download the generated report

## Technologies Used

- Python
- Streamlit
- Ollama
- Llama 3.2
- PyPDF
- Prompt Engineering

## Project Structure

```text
LegalDocumentAnalyzer/
├── app.py
├── input_module.py
├── preprocessing_module.py
├── prompt_module.py
├── analyzer_module.py
├── save_module.py
├── requirements.txt
├── .gitignore
└── outputs/
    └── legal_analysis.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/URK23CS1214/Legal-Document-Analyzer.git
cd Legal-Document-Analyzer
```

Create and activate a virtual environment on Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama from https://ollama.com/ and download the model:

```bash
ollama pull llama3.2
```

## Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## Workflow

1. Input or upload a legal document.
2. Preprocess the document text.
3. Generate an AI analysis prompt.
4. Analyze the document using the local LLM.
5. Display the summary and important clauses.
6. Save or download the analysis report.

## Disclaimer

This application is intended for educational and informational purposes only. It does not replace professional legal advice. Always verify extracted information against the original document.

## Author

**URK23CS1214**

Computer Science Engineering