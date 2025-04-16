# 🩺 Medical Semantic Search

This project is a semantic search engine for medical text. User questions are converted into embeddings and matched against a Weaviate vector database to retrieve the most semantically relevant answers.

## 🚀 Features

- Frontend built with Streamlit
- FastAPI backend for semantic search
- Weaviate vector database integration (containerized via Docker)
- Embeddings generated using HuggingFace SentenceTransformer
- Ranked results with answer and source display

---

## 📁 Project Structure

    \---medical-search-case      
        |   .gitignore
        |   docker-compose.yml   
        |   requirements.txt     
        |   
        +---backend
        |   |   app.py
        |   |   data_loader.py   
        |   |   Dockerfile       
        |   |   embedding.py     
        |   |   requirements.txt 
        |   |   schema.json      
        |   |   start.sh
        |   |   weaviate_client.py
        |   |
        |
        +---data
        |       train-00000-of-00001.parquet
        |
        +---frontend
        |       Dockerfile
        |       requirements.txt
        |       search_ui.py
        |
        \---weaviate
                docker-compose.yml
                schema.json

---

## ⚙️ Setup & Running the App

### 1. Requirements

- Docker
- Python 3.11+ (only for development mode)

### 2. To run with Docker

git clone https://github.com/123162/task-solution.git
cd task-solution
docker compose up --build

🌐 Accessing the App
Frontend UI (Streamlit): http://localhost:8501

FastAPI Docs: http://localhost:8000/docs

Weaviate Console (optional): http://localhost:8080

🔍 Example Query
Endpoint: POST /search

Request Body:

json
{
  "query": "Which bacteria cause strep throat?"
}

👩‍💻 Developer Notes
Developed with FastAPI and served via Uvicorn.

Embeddings are generated on the CPU. For large-scale deployments, consider using GPU-based infrastructure.

Weaviate is launched via Docker Compose and accessed via gRPC.


ATTENTION: 
The backend container will automatically initialize the Weaviate schema and upload the dataset to Weaviate by running weaviate_client.py and data_loader.py inside start.sh.

This process may take a little time, especially during the first startup, as it performs bulk vector embedding and upload operations.

