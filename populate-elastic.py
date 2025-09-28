import datetime
from uuid import uuid4
import os

from elasticsearch import Elasticsearch
from dotenv import load_dotenv
load_dotenv()

es = Elasticsearch("http://localhost:9200")

if not es.ping():
    raise ValueError("Elasticsearch is not responding")

print("Connected to Elasticsearch!")

# Define index name
index_name = os.environ["INDEX_NAME"]

# Sample documents to insert
unix_timestamp = datetime.datetime.now(datetime.UTC)
documents = [
    {"title": "First Document", "content": "This is the first document", "@timestamp": unix_timestamp},
    {"title": "Second Document", "content": "Second document content goes here", "@timestamp": unix_timestamp},
    {"title": "Elasticsearch", "content": "Elasticsearch is a powerful search engine", "@timestamp": unix_timestamp},
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
