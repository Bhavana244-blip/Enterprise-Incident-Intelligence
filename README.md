
# Enterprise Incident Intelligence System  
**GenAI-Ready AIOps Decision Support Platform**

🔗 **Live Demo:** https://enterprise-incident-intelligence.streamlit.app/

---

## Overview

The **Enterprise Incident Intelligence System** is an AI-powered decision support platform designed to help engineers resolve production incidents faster by reusing knowledge from similar historical incidents.

In large organizations, incident knowledge is often fragmented across tickets, postmortems, and internal documentation. When new incidents occur, engineers spend valuable time searching for relevant past cases. This system addresses that gap by transforming historical incident data into reusable operational intelligence.

---

## Problem Statement

Modern production systems generate a high volume of incidents. While organizations store incident reports and postmortems, this knowledge is rarely leveraged effectively during active outages.

Key challenges:
- Incident knowledge is scattered across multiple systems  
- Searching past incidents is manual and time-consuming  
- Junior engineers lack access to historical operational context  
- Mean Time To Resolution (MTTR) remains high  

---

## Solution

This project implements an **enterprise-style incident intelligence workflow** that:

1. Converts historical incident reports into semantic embeddings  
2. Stores them in a vector database for meaning-based retrieval  
3. Finds the most relevant past incidents for a new issue  
4. Generates a structured incident analysis with root cause, resolution steps, and preventive actions  
5. Exposes the system through a REST API and a professional web interface  

The architecture follows **Retrieval-Augmented Generation (RAG)** principles and is designed to be **GenAI-ready** for future LLM integration.

---

## Architecture

Web UI (Streamlit)
↓
FastAPI Backend (REST API)
↓
Semantic Retrieval Layer
(FAISS + Embeddings)
↓
Incident Reasoning Engine
(GenAI-ready, pluggable)


---

## Tech Stack

**Backend**
- FastAPI
- Python

**Frontend**
- Streamlit (enterprise-style internal dashboard)

**AI / ML**
- SentenceTransformers (local embeddings)
- FAISS (vector database)
- Retrieval-Augmented Generation (RAG) architecture

**Deployment**
- Streamlit Cloud (frontend)
- Modular backend suitable for containerization

---

## Key Features

- Semantic search over historical incident data  
- Retrieval of contextually similar past incidents  
- Structured incident analysis reports  
- Enterprise-style web interface for on-call engineers  
- Clean, modular backend design  
- GenAI-ready reasoning layer (LLM-pluggable)

---

## Live Demo

The deployed application allows users to:
- Enter a production incident description  
- Trigger semantic retrieval of similar historical incidents  
- View a structured incident analysis report in real time  

🔗 **Demo URL:** https://enterprise-incident-intelligence.streamlit.app/



## Running Locally

### 1. Start the Backend
```bash
uvicorn backend.app.main:app --reload
```
### 2. Start the Frontend
```
streamlit run frontend/app.py
```

### Design Decisions
---
Semantic retrieval over keyword search to capture intent, not just text matches

Local embeddings to reduce cost and avoid vendor lock-in

Pluggable reasoning layer to support future integration with enterprise LLMs

Simple, functional UI aligned with internal enterprise tools rather than consumer apps

### Future Enhancements
---

Integration with ServiceNow / Jira incident data

Enterprise LLM integration (IBM Watson, Azure OpenAI, etc.)

Role-based access control

Incident confidence scoring and re-ranking

Post-incident learning and automated knowledge updates

### Author Notes
---
This project was built as a focused enterprise-style MVP to demonstrate applied AI system design, semantic retrieval, and operational intelligence workflows. The emphasis is on architectural clarity, real-world relevance, and explainability rather than feature bloat.

### Disclaimer

This is a demonstration system using sample incident data. It is not connected to real production environments.


