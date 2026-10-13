# Guitar Theory RAG Assistant

## Context

Build a small Python RAG application that answers guitar theory questions using a personal Markdown knowledge base. This is a learning project focused on understanding embeddings, retrieval, vector databases, and LLM integration.

## Technologies

- Python
- Sentence Transformers for local embeddings
- ChromaDB for vector storage
- OpenAI API for answer generation
- PyYAML to parse the YAML
- txt for knowledge documents

## Thought process

- I will use AI as a collaboration assistant for this project, but not for code gen, as I am trying to learn this problem-set. Not against code-gen, but in learning I like to write solutions myself.
- I try to always start with the tightest smallest working version that will solve some part of the problem.
- Small commits will show the journey

## Initial project plan

1. Set up project structure, init packages and technologies, then hello world an output
2. Collect the external data that will be used for RAG, and a way to parse it
3. Set up ingestion pipeline
4. Generate Embeddings - numerical representations of the data
5. Build the vector database
6. Implement retrieval setup
7. Connect LLM
8. Connect to the CLI
9. Add a couple UX niceties like loading, but don't go overboard
10. Adjust the prompt till it works well

## Ways to improve - Endless, only so many hours in the day

1. Make a nice UI or add better CLI UX
2. Give it more data, or setup an API connection to retrieve data also
3. Learn Python best practices for codebase architecture
4. Better project organization
5. Go beyond basic RAG with other features
