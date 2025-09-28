import datetime
from uuid import uuid4

from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

if not es.ping():
    raise ValueError("Elasticsearch is not responding")

print("Connected to Elasticsearch!")

# Define index name
index_name = "demo-data"

# Sample documents to insert
documents = [
    {"title": "First Document", "content": "This is the first document", "timestamp": datetime.datetime.now()},
    {"title": "Second Document", "content": "Second document content goes here", "timestamp": datetime.datetime.now()},
    {"title": "Elasticsearch", "content": "Elasticsearch is a powerful search engine", "timestamp": datetime.datetime.now()},
]

# Create index (if not exists)
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    print(f"Created index '{index_name}'")

# Index the documents
for doc in documents:
    doc_id = str(uuid4())
    res = es.index(index=index_name, id=doc_id, document=doc)
    print(f"Inserted doc ID {doc_id}: {res['result']}")

print("Finished populating Elasticsearch.")
