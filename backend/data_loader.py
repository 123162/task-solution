# upload_to_weaviate.py

import sys
import os
import pandas as pd
from tqdm import tqdm
from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from embedding import embed_text

# connect to Weaviate client
client = WeaviateClient(
    connection_params=ConnectionParams.from_params(
        http_host="weaviate",
        http_port=8080,
        http_secure=False,
        grpc_host="weaviate",
        grpc_port=50051,
        grpc_secure=False
    )
)
client.connect()

# Read data file
df = pd.read_parquet("/app/data/train-00000-of-00001.parquet")

# Get the collection
collection = client.collections.get("MedicalQuestion")

# Load data to Weaviate
for _, row in tqdm(df.iterrows(), total=len(df), desc="📦 Uploading medical data"):
    full_text = row.get("data", "").strip()

    if not full_text:
        continue

    vector = embed_text(full_text)

    collection.data.insert(
        properties={
            "question": full_text,
            "answer": "",  
            "source": ""
        },
        vector=vector
    )

    print(f"✅ Added: {full_text[:60]}...")

client.close()
