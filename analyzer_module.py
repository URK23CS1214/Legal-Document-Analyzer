
import ollama


def analyze_legal_document(prompt):

    response=ollama.chat(
        model="llama3.2:latest",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        options={
            "num_ctx":2048
        }
    )

    return response["message"]["content"]
