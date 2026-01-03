import os
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

DATA_PATH = "backend/data/incidents"
VECTOR_STORE_PATH = "backend/vector_store"

def ingest_incidents():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(DATA_PATH, file))
            documents.extend(loader.load())

    # FORCE local embeddings (no OpenAI)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local(VECTOR_STORE_PATH)

    print(f"Ingested {len(documents)} incident documents using LOCAL embeddings.")

if __name__ == "__main__":
    ingest_incidents()
