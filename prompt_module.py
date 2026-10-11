
def create_legal_prompt(document):

    prompt=f"""
You are a legal document analysis assistant.

Analyze the legal document provided below.

Extract the following information:

1. Document Type
2. Parties Involved
3. Purpose of the Agreement
4. Obligations of Each Party
5. Payment Terms
6. Duration
7. Termination Conditions
8. Important Dates
9. Confidentiality Clauses
10. Liability Clauses
11. Intellectual Property Clauses
12. Dispute Resolution
13. Governing Law
14. Concise Summary

Important instructions:
- Use only information present in the document.
- Do not invent facts or missing details.
- If information is unavailable, write
  "Not mentioned in the document."
- Present the analysis using clear headings
  and bullet points.
- This analysis is informational and is not
  professional legal advice.

LEGAL DOCUMENT:

{document}
"""

    return prompt
