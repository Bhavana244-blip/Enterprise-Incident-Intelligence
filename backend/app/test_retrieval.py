from retriever import retrieve_similar_incidents

query = "Payments are slow and failing during high traffic"

results = retrieve_similar_incidents(query)

print("Similar incidents found:\n")
for i, doc in enumerate(results, start=1):
    print(f"--- Incident {i} ---")
    print(doc.page_content)
