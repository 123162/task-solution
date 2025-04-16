from weaviate import WeaviateClient
from weaviate.connect import ConnectionParams
from weaviate.classes.config import DataType
import json
import os

# Connection
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

# Schema file
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.json")

def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = json.load(f)

    # dataType map
    data_type_map = {
        "text": DataType.TEXT,
        "int": DataType.INT,
        "number": DataType.NUMBER,
        "boolean": DataType.BOOL,
        "date": DataType.DATE
    }

    for class_def in schema["classes"]:
        class_name = class_def["class"]

        # ❗ Delete old collection
        if client.collections.exists(class_name):
            print(f"🗑 Koleksiyon siliniyor: {class_name}")
            client.collections.delete(class_name)

        # ✅ Create new collection
        print(f"➕ Creating collection: {class_name}")
        client.collections.create(
            name=class_name,
            properties=[
                {
                    "name": prop["name"],
                    "data_type": data_type_map.get(prop["dataType"][0], DataType.TEXT)
                }
                for prop in class_def["properties"]
            ],
            description=class_def.get("description", ""),
            vectorizer_config=None
        )

if __name__ == "__main__":
    if client.is_ready():
        print("Weaviate is running ✅")
        load_schema()
    else:
        print("❌ Weaviate not reachable.")
    client.close()
