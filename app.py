
import streamlit as st

from input_module import get_legal_document
from preprocessing_module import preprocess_document
from prompt_module import create_legal_prompt
from analyzer_module import analyze_legal_document
from save_module import save_analysis


st.set_page_config(
    page_title="Legal Document Analyzer",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ Automated Legal Document Analyzer")
st.write(
    "Analyze legal documents, summarize important terms, "
    "and identify key clauses using local AI."
)

st.warning(
    "This tool provides informational summaries only. "
    "It does not replace advice from a qualified lawyer."
)

document=get_legal_document()

if st.button("Analyze Legal Document",type="primary"):

    if not document.strip():
        st.warning("Please enter or upload a legal document.")

    else:

        with st.spinner("Analyzing document with Llama 3.2..."):

            cleaned_document=preprocess_document(document)

            prompt=create_legal_prompt(cleaned_document)

            analysis=analyze_legal_document(prompt)

            st.session_state["legal_analysis"]=analysis

if "legal_analysis" in st.session_state:

    st.header("📋 Legal Document Analysis")

    st.markdown(st.session_state["legal_analysis"])

    if st.button("💾 Save Analysis"):

        filename=save_analysis(
            st.session_state["legal_analysis"]
        )

        st.success("Report saved to "+filename)

        with open(filename,"rb") as file:

            st.download_button(
                "Download Report",
                data=file,
                file_name="legal_analysis.txt",
                mime="text/plain"
            )
