from tools.health import fetch_health
from tools.metrics import fetch_metrics
from tools.logs import fetch_logs


def detect_incidents():

    incidents = []

    health = fetch_health()

    metrics = fetch_metrics()

    logs = fetch_logs()

    for item in health:

        if item["type"] == "pod":

            status = item.get("status")

            restarts = item.get("restarts", 0)

            pod_name = item.get("pod")

            if status != "Running":

                incidents.append(
                    {
                        "severity": "SEV-1",
                        "issue": f"Pod {pod_name} is not running"
                    }
                )

            if restarts >= 1:

                incidents.append(
                    {
                        "severity": "SEV-2",
                        "issue": f"Pod {pod_name} has high restart count"
                    }
                )

        elif item["type"] == "deployment":

            deployment_name = item.get("deployment")

            desired = item.get("desired_replicas", 0)

            available = item.get("available_replicas", 0)

            if desired < available:

                incidents.append(
                    {
                        "severity": "SEV-1",
                        "issue": f"Deployment {deployment_name} replica mismatch ({available}/{desired})"
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

    print(incidents)

    return incidents