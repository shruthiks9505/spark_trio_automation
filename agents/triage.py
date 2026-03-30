def triage_agent(alert):
    if "ERROR" in alert or "timeout" in alert.lower():
        return {"is_real": True, "confidence": 0.92}
    return {"is_real": False, "confidence": 0.30}