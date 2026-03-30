import streamlit as st
from agent_smith import agent_smith
from agents.executor import execute_action

st.title("Autonomous Incident Resolution Agent")

# Inject failure
if st.button("Inject DB Failure"):
    alert = "ERROR: Database connection timeout"

    st.error(f"Alert: {alert}")

    result = agent_smith(alert)

    # Show AI Analysis
    st.subheader("AI Analysis")
    st.write(
        f"Real Incident: {result['triage']['is_real']} "
        f"(Confidence: {result['triage']['confidence']})"
    )

    st.write(f"Type: {result['classification']['type']}")
    st.write(f"Severity: {result['classification']['severity']}")

    # Recommendation
    st.subheader("Recommendation")
    st.write(f"Action: {result['recommendation']['action']}")
    st.write(f"Confidence: {result['recommendation']['confidence']}")
    st.write(f"Reason: {result['recommendation']['reason']}")

    # Reasoning
    st.subheader("Agent Smith Reasoning")
    for step in result["reasoning"]:
        st.write(f"→ {step}")

    # Approval
    if st.button("Approve & Execute"):
        output = execute_action(result['recommendation']['action'])
        st.success(output)

        st.subheader("Audit Log")
        st.write("Incident resolved successfully")

    #success