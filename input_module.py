
import streamlit as st


def get_legal_document():

    st.subheader("📄 Legal Document Input")

    input_method=st.radio(
        "Choose input method",
        ["Enter Text","Upload File"],
        horizontal=True
    )

    document=""

    if input_method=="Enter Text":

        document=st.text_area(
            "Paste your legal document",
            height=250,
            placeholder="Paste the contract or legal agreement here..."
        )

    else:

        uploaded_file=st.file_uploader(
            "Upload a TXT or PDF file",
            type=["txt","pdf"]
        )

        if uploaded_file is not None:

            if uploaded_file.name.endswith(".txt"):
                document=uploaded_file.read().decode(
                    "utf-8",
                    errors="ignore"
                )

            elif uploaded_file.name.endswith(".pdf"):
                from pypdf import PdfReader

                reader=PdfReader(uploaded_file)

                pages=[]

                for page in reader.pages:
                    pages.append(page.extract_text() or "")

                document="\n".join(pages)

    return document
