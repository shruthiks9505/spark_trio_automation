def recommend_fix(alert, runbook):
    return {
        "action": "Restart Database Service",
        "confidence": 0.87,
        "reason": "Matched runbook for DB timeout"
    }