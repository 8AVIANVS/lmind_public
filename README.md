# LMIndex RAG

A document question-answering system built with LlamaIndex that converts PDF documents to markdown, indexes their content, and enables natural language queries against the document content.

## Overview

This project allows you to:
1. Convert PDF documents to markdown format
2. Parse and index document content using LlamaIndex
3. Create a vector-based retrieval system for semantic search
4. Query the indexed documents using natural language questions

## Requirements

- Python 3.8+
- OpenAI API key

## Dependencies

- llama_index
- markitdown
- python-dotenv
- openai

## Setup

1. Clone this repository

2. Install the required dependencies:
   ```
   pip install llama-index markitdown python-dotenv openai
   ```

3. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Place your PDF document as `input.pdf` in the root directory.

2. Run the main script:
   ```
   python main.py
   ```

3. The script will:
   - Convert the PDF to markdown and save it in `data/output.md`
   - Index the document content
   - Start an interactive question-answering session

4. Ask questions about the document content to retrieve relevant information.

## Project Structure

```
LMIndex_P/
│
├── main.py           # Main application script
├── input.pdf         # Input PDF document to process
├── .env              # Environment variables (containing API keys)
│
├── data/             # Directory for processed documents
│   └── output.md     # Converted markdown document
│
└── pipeline_storage/ # Storage for the ingestion pipeline cache
```

## How It Works

1. **PDF Conversion**: The PDF document is converted to markdown format for better text extraction.

2. **Document Processing**:
   - The document is split into manageable chunks
   - Titles are extracted
   - Text is embedded using OpenAI embeddings

3. **Indexing**: LlamaIndex creates a vector store for semantic search.

4. **Query Engine**: Query engine and retriever allow asking questions about the document.

5. **Retrieval**: When you ask a question, the system:
   - Finds the most relevant document chunks
   - Provides the answer
   - Shows detailed information about the retrieved nodes