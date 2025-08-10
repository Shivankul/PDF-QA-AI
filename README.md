# PDF-QA-AI

A web application that allows you to upload a PDF and ask questions about its content—answers are generated using AI and are strictly based on the information found in the uploaded document.

## Features

- **PDF Upload**: Easily upload any PDF file for analysis.
- **Contextual Q&A**: Ask questions, and the system retrieves relevant answers solely from the uploaded PDF.
- **Code-friendly Answers**: If your question is about code, the assistant provides concise code examples based on the PDF's content.
- **User-Friendly UI**: Built with Streamlit for a simple, interactive experience.
- **Robust Backend**: Uses FastAPI and LangChain for efficient document processing and AI integration.

## How It Works

1. **Upload a PDF**: The document is split into manageable chunks and embedded using OpenAI's embedding models.
2. **Ask Questions**: Queries are matched to relevant chunks using vector similarity search (Qdrant).
3. **AI-Powered Responses**: A GPT-4o model generates answers based strictly on the extracted context from your PDF.

## Technologies Used

- **Python**
- **FastAPI** (backend API)
- **Streamlit** (frontend UI)
- **LangChain** (document processing & retrieval)
- **Qdrant** (vector storage & similarity search)
- **OpenAI GPT-4o** (AI model for answering questions)

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Shivankul/PDF-QA-AI.git
   cd PDF-QA-AI
