from agents.triage import triage_agent
from agents.classifier import classify_agent
from agents.rag import rag_agent
from agents.recommender import recommend_fix

def agent_smith(alert):
    reasoning = []

    triage = triage_agent(alert)
    reasoning.append(f"Triage: {triage}")

    if not triage["is_real"]:
        return {"final": "Noise Alert", "reasoning": reasoning}

    classification = classify_agent(alert)
    reasoning.append(f"Classification: {classification}")

    runbook = rag_agent(alert)
    reasoning.append(f"Runbook Matched")

    recommendation = recommend_fix(alert, runbook)
    reasoning.append(f"Recommendation Generated")

    return {
        "triage": triage,
        "classification": classification,
        "runbook": runbook,
        "recommendation": recommendation,
        "reasoning": reasoning
    }