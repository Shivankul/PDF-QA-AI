import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000" 

st.set_page_config(page_title="RAG QA with PDF", page_icon="🤖", layout="wide")

st.title("📄 RAG PDF QA Assistant")
st.markdown("Upload a PDF and ask questions — answers are retrieved only from the document.")

# PDF Upload Section
st.header("1️⃣ Upload your PDF")
uploaded_pdf = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_pdf is not None:
    if st.button("Upload & Process PDF"):
        files = {"file": uploaded_pdf}
        with st.spinner("Uploading and processing..."):
            res = requests.post(f"{FASTAPI_URL}/upload_pdf", files=files)
        if res.status_code == 200:
            st.success(res.json().get("message", "PDF processed successfully!"))
        else:
            st.error("Failed to upload PDF. Check server logs.")

# Question Section
st.header("2️⃣ Ask a Question")
question = st.text_area("Type your question here...")

if st.button("Get Answer"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            res = requests.post(
                f"{FASTAPI_URL}/ask",
                data={"question": question}
            )
        if res.status_code == 200:
            answer = res.json().get("answer", "No answer returned.")
            st.markdown("### 💬 Answer:")
            st.write(answer)
        else:
            st.error("Error getting answer from backend.")
