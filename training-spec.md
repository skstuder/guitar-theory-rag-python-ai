# Guitar Theory RAG Assistant

## Context

Build a small Python RAG application that answers guitar theory questions using a personal Markdown knowledge base. This is a learning project focused on understanding embeddings, retrieval, vector databases, and LLM integration.

## Technologies

- Python
- Sentence Transformers for local embeddings
- ChromaDB for vector storage
- OpenAI API for answer generation
- Markdown for knowledge documents

## Thought process

- I will use AI as a collaboration assistant for this project, but not for code gen, as I am trying to learn this problem-set. Not against code-gen, but in learning I like to write solutions myself.
- I try to always start with the tightest smallest working version that will solve some part of the problem.

## Initial project plan

1. Set up project structure, init packages and technologies, then hello world an output
2. Collect the external data that will be used for RAG
3. Set up ingestion pipeline
4. Generate Embeddings
5. Build the vector database
6. Implement retrieval
7. Connect LLM
8. Connect to the CLI
