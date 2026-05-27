from tools.health import fetch_health
from tools.metrics import fetch_metrics
from tools.logs import fetch_logs


def detect_incidents():

    incidents = []

    health = fetch_health()

    metrics = fetch_metrics()

    logs = fetch_logs()


    for pod in health:

        status = pod.get("status")

        restarts = pod.get("restarts", 0)

        pod_name = pod.get("pod")


        if status != "Running":

            incidents.append(
                {
                    "severity": "SEV-1",
                    "issue": f"Pod {pod_name} is not running"
                }
            )


        if restarts > 3:

            incidents.append(
                {
                    "severity": "SEV-2",
                    "issue": f"Pod {pod_name} has high restart count"
                }
            )


    for log in logs:

        log_text = str(
            log.get("log", "")
        ).lower()


        if "error" in log_text:

            incidents.append(
                {
                    "severity": "SEV-2",
                    "issue": "Error logs detected"
                }
            )


        if "503" in log_text:

            incidents.append(
                {
                    "severity": "SEV-1",
                    "issue": "HTTP 503 service failures detected"
                }
            )


    return incidents