import os
import json

from dotenv import load_dotenv
from ai.incident_detector import detect_incidents

import google.generativeai as genai

from tools.health import fetch_health
from tools.metrics import fetch_metrics
from tools.logs import fetch_logs


load_dotenv()


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
    "gemini-3.5-flash"
)


def analyze_cluster(question):

    health = fetch_health()

    metrics = fetch_metrics()

    logs = fetch_logs()

    incidents = detect_incidents()

    prompt = f"""
You are KIRA, an elite AI Site Reliability Engineer.

Your responsibilities:
- Analyze Kubernetes telemetry
- Detect failures
- Identify anomalies
- Estimate incident severity
- Recommend remediation
- Think like a production SRE

User Question:
{question}

Kubernetes Health:
{json.dumps(health, indent=2)}

Prometheus Metrics:
{json.dumps(metrics, indent=2)}

Recent Loki Logs:
{json.dumps(logs, indent=2)}

Active Incidents:
{incidents}

Instructions:

1. Analyze cluster behavior carefully.
2. Detect unhealthy trends.
3. Identify suspicious pod behavior.
4. Correlate logs + metrics + pod states.
5. Estimate incident severity:
   - SEV-1
   - SEV-2
   - SEV-3
   - INFO
6. Explain WHY the issue occurs.
7. Suggest exact kubectl troubleshooting commands.
8. Suggest remediation steps.
9. Keep response structured and professional.

Return response in this format:

# Cluster Summary

# Key Findings

# Severity Assessment

# Root Cause Analysis

# Recommended Remediation

# Preventative Measures

# Exact kubectl Commands to diagnose and fix the issue

"""

    response = model.generate_content(
        prompt
    )

    return response.text


if __name__ == "__main__":

    question = input(
        "Ask KIRA: "
    )

    result = analyze_cluster(
        question
    )

    print("\n")

    print(result)