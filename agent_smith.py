from agents.triage import triage_agent
from agents.classifier import classify_agent
from agents.rag import rag_agent
from agents.recommender import recommend_fix


def agent_smith(alert):
    reasoning = []

    # Step 1: Triage
    triage = triage_agent(alert)
    reasoning.append(f"Triage: {triage}")

    if not triage["is_real"]:
        return {
            "final": "Noise Alert",
            "reasoning": reasoning
        }

    # Step 2: Classification
    classification = classify_agent(alert)
    reasoning.append(f"Classification: {classification}")

    # Step 3: Runbook (RAG)
    runbook = rag_agent(alert)
    reasoning.append("Runbook Matched")

    # Step 4: Recommendation
    recommendation = recommend_fix(alert, runbook)
    reasoning.append("Recommendation Generated")

    # Final Output
    return {
        "triage": triage,
        "classification": classification,
        "runbook": runbook,
        "recommendation": recommendation,
        "reasoning": reasoning
    }