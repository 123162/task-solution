from sentence_transformers import SentenceTransformer
import numpy as np

# Load the model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(text: str) -> list:

    embedding = model.encode(text)
    return embedding.tolist() 
