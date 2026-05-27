import subprocess


def fetch_logs(namespace="boutique"):

    command = [
        "kubectl",
        "logs",
        "-n",
        namespace,
        "deployment/orders",
        "--tail=20"
    ]

    try:

        result = subprocess.check_output(
            command,
            text=True
        )

        lines = result.splitlines()

        return [
            {
                "log": line
            }
            for line in lines
        ]

    except Exception as e:

        return [
            {
                "log": str(e)
            }
        ]