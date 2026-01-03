from fastapi import FastAPI
from .schemas import IncidentRequest, IncidentResponse
from .retriever import retrieve_similar_incidents
from .generator import generate_incident_analysis


app = FastAPI(
    title="Enterprise Incident Intelligence System",
    description="GenAI-powered incident analysis and resolution support",
    version="1.0"
)

@app.get("/")
def health_check():
    return {"status": "running"}

@app.post("/analyze-incident", response_model=IncidentResponse)
def analyze_incident(request: IncidentRequest):
    docs = retrieve_similar_incidents(request.description)
    analysis = generate_incident_analysis(request.description, docs)
    return {"analysis": analysis}
