from fastapi import FastAPI
from pydantic import BaseModel
from backend.embedding import embed_text
from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

client = WeaviateClient(
    connection_params=ConnectionParams.from_params(
        http_host="localhost",
        http_port=8080,
        http_secure=False,
        grpc_host="localhost",
        grpc_port=50051,
        grpc_secure=False
    )
)
client.connect()
collection = client.collections.get("MedicalQuestion")

@app.post("/search")
def search(req: QueryRequest):
    vector = embed_text(req.query)

    results = collection.query.near_vector(
        near_vector=vector,
        return_metadata=["distance"],
        return_properties=["question", "answer", "source"],
        limit=5
    )

    return {
        "query": req.query,
        "results": [
            {
                "score": round(obj.metadata.distance, 3),
                "question": obj.properties.get("question"),
                "answer": obj.properties.get("answer"),
                "source": obj.properties.get("source")
            }
            for obj in results.objects
        ]
    }
