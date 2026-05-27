import random


def fetch_metrics():

    return {
        "cpu_usage": f"{random.randint(20, 80)}%",
        "memory_usage": f"{random.randint(30, 90)}%",
        "active_pods": random.randint(5, 15)
    }