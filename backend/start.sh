#!/bin/bash
set -x  # Debug mode

echo "⏳ Waiting for Weaviate to be ready..."
sleep 5

echo "🚀 Loading schema..."
python weaviate_client.py

echo "🌀 Starting backend API..."

# sleep ve load schema again
sleep 3
echo "🔁 Re-loading schema (just in case)..."
python weaviate_client.py
python data_loader.py

# starting uvicorn
exec uvicorn app:app --host 0.0.0.0 --port 8000

