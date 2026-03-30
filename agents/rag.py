def rag_agent(alert):
    with open("data/runbook.txt", "r") as f:
        return f.read()