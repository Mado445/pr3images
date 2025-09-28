import os
import time
import random
import requests

# Service URL (from env or default)
ECHO_URL = os.getenv("ECHO_URL", "http://echo-svc:8080")

# PVC mount paths (fixed in Pod spec)
PVC_A_PATH = os.environ["PVC_A_PATH"]
PVC_B_PATH = os.environ["PVC_B_PATH"]

while True:
    n1, n2 = random.randint(1, 100), random.randint(1, 100)
    # Send both numbers to echo service
    try:
        r = requests.post(ECHO_URL, json={"n1": n1, "n2": n2})
        print(f"Sent {n1}, {n2} → status {r.status_code}")
    except Exception as e:
        print("Error:", e)

    # Append to both PVC files
    with open(PVC_A_PATH, "a") as f:
        f.write(f"{n1},{n2}\n")
    with open(PVC_B_PATH, "a") as f:
        f.write(f"{n1},{n2}\n")

    time.sleep(10)
