import subprocess
import json


def fetch_health(namespace="boutique"):

    command = [
        "kubectl",
        "get",
        "pods",
        "-n",
        namespace,
        "-o",
        "json"
    ]

    result = subprocess.check_output(command)

    pods_data = json.loads(result)

    health = []

    for pod in pods_data["items"]:

       health.append(
       {
        "type": "pod",
        "name": pod["metadata"]["name"],
        "status": pod["status"]["phase"]
    }
    )

    return health