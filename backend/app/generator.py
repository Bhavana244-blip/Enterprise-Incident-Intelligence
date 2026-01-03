def generate_incident_analysis(query: str, retrieved_docs):
    """
    Generates a structured incident analysis using retrieved historical incidents.
    This version uses rule-guided reasoning (enterprise-safe fallback).
    """

    # context = "\n\n".join([doc.page_content for doc in retrieved_docs])
    context = "\n\n".join(
    f"Relevant Incident:\n{doc.page_content}" for doc in retrieved_docs
)


    analysis = f"""
INCIDENT ANALYSIS REPORT
------------------------

New Incident:
{query}

Similar Historical Incidents:
{context}

Likely Root Cause:
Based on similar incidents, the issue is likely caused by resource exhaustion,
misconfiguration, or insufficient scaling during peak load.

Recommended Resolution Steps:
- Review system metrics during peak traffic
- Check database / queue / service capacity
- Apply scaling or configuration fixes similar to past incidents

Preventive Actions:
- Improve alert thresholds
- Add load testing before high-traffic events
- Automate capacity scaling rules
"""

    return analysis
