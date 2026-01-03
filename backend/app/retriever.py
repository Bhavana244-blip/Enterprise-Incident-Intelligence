from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
import os

# ---------------- SAMPLE INCIDENT DATA ----------------
INCIDENTS = [
    {
        "id": "INC-001",
        "service": "Payments API",
        "severity": "High",
        "issue": "Transactions failing and high latency during peak hours",
        "root_cause": "Database connection pool exhaustion",
        "resolution": "Increased DB pool size, enabled caching, scaled read replicas",
        "prevention": "Improved traffic alerts and auto-scaling"
    },
    {
        "id": "INC-002",
        "service": "Authentication Service",
        "severity": "Medium",
        "issue": "Intermittent login failures",
        "root_cause": "Load balancer health check misconfiguration",
        "resolution": "Fixed health checks and stabilized LB rules",
        "prevention": "Deployment validation checks"
    },
    {
        "id": "INC-003",
        "service": "Order Processing Service",
        "severity": "High",
        "issue": "Order creation timing out during campaigns",
        "root_cause": "Message queue backlog",
        "resolution": "Scaled consumers and optimized queue processing",
        "prevention": "Queue depth monitoring and load testing"
    }
]

# ---------------- EMBEDDINGS ----------------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------- BUILD VECTOR STORE AT RUNTIME ----------------
def build_vectorstore():
    docs = []
    for inc in INCIDENTS:
        content = f"""
Incident ID: {inc['id']}
Service: {inc['service']}
Severity: {inc['severity']}
Issue: {inc['issue']}
Root Cause: {inc['root_cause']}
Resolution: {inc['resolution']}
Preventive Actions: {inc['prevention']}
"""
        docs.append(Document(page_content=content))

    return FAISS.from_documents(docs, embeddings)

# ---------------- RETRIEVER ----------------
def retrieve_similar_incidents(query: str, k: int = 3):
    vectorstore = build_vectorstore()
    return vectorstore.similarity_search(query, k=k)
