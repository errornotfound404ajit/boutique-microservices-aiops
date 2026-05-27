import streamlit as st

from ai.gemini_agent import analyze_cluster
from report_generator import generate_incident_report
from ai.incident_detector import detect_incidents

from tools.health import fetch_health
from tools.metrics import fetch_metrics
from tools.logs import fetch_logs


st.set_page_config(
    page_title="KIRA AIOps",
    page_icon="🤖",
    layout="wide"
)

st.sidebar.button("Refresh Telemetry")

st.title("🤖 KIRA - AI Ops Assistant")


st.sidebar.header("Cluster Overview")


health = fetch_health()
metrics = fetch_metrics()
logs = fetch_logs()


total_pods = len(health)

healthy_pods = len(
    [
        pod for pod in health
        if pod.get("status") == "Running"
    ]
)


st.sidebar.metric(
    "Total Pods",
    total_pods
)

st.sidebar.metric(
    "Healthy Pods",
    healthy_pods
)

st.sidebar.metric(
    "Recent Logs",
    len(logs)
)


if "messages" not in st.session_state:

    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


question = st.chat_input(
    "Ask KIRA about your cluster..."
)


if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "KIRA is analyzing telemetry..."
        ):

            try:

                response = analyze_cluster(
                    question
                )

                report_file = generate_incident_report(
                   response
               )

                with open(report_file, "rb") as pdf_file:

                     st.download_button(
                     label="Download Incident Report",
                     data=pdf_file,
                     file_name=report_file.split("/")[-1],
                     mime="application/pdf"
                    )

                if "SEV-1" in response:
                    st.error(response)
                elif "SEV-2" in response:
                    st.warning(response)
                else:
                    st.success(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                error_message = f"""
Error analyzing cluster:

{str(e)}
"""

                st.error(error_message)


with st.expander("📜 Recent Logs"):

    st.json(logs)


with st.expander("📊 Metrics Snapshot"):

    st.json(metrics)


with st.expander("❤️ Cluster Health"):

    st.json(health)


incidents = detect_incidents()


st.sidebar.header("Active Incidents")


if incidents:

    for incident in incidents:

        severity = incident["severity"]

        issue = incident["issue"]


        if severity == "SEV-1":

            st.sidebar.error(issue)

        elif severity == "SEV-2":

            st.sidebar.warning(issue)

        else:

            st.sidebar.info(issue)

else:

    st.sidebar.success(
        "No active incidents"
    )