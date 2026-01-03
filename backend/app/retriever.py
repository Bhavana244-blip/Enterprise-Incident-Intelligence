from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_STORE_PATH = "backend/vector_store"

def retrieve_similar_incidents(query: str, k: int = 1):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    results = vectorstore.similarity_search(query, k=k)
    return results
