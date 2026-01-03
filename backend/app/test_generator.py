from retriever import retrieve_similar_incidents
from generator import generate_incident_analysis

query = "Payments are failing and latency is very high during traffic spikes"

docs = retrieve_similar_incidents(query)
result = generate_incident_analysis(query, docs)

print(result)
