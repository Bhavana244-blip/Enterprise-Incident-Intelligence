from pydantic import BaseModel

class IncidentRequest(BaseModel):
    description: str

class IncidentResponse(BaseModel):
    analysis: str
