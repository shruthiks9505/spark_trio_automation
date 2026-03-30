def classify_agent(alert):
    if "database" in alert.lower():
        return {"type": "Database Failure", "severity": "High"}
    return {"type": "Unknown", "severity": "Low"}