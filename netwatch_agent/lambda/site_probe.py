import urllib.request
import time
import json
import boto3
import os

# CloudWatch client for pushing custom metrics
cw_client = boto3.client("cloudwatch")
METRIC_NAMESPACE = "NetWatchMetrics"

def probe_url(target: str, timeout_sec: int = 10):
    """
    Check a website's availability and response time.
    Returns: (status_flag, latency_ms) where status_flag = 1 if reachable, else 0.
    """
    start_time = time.time()
    try:
        response = urllib.request.urlopen(target, timeout=timeout_sec)
        latency_ms = (time.time() - start_time) * 1000.0
        status_flag = 1 if response.status == 200 else 0
        return status_flag, latency_ms
    except Exception as err:
        print(f"[WARN] Unable to reach {target}: {err}")
        return 0, None

def push_metrics(target: str, status_flag: int, latency_ms: float | None):
    """
    Send custom metrics for availability and latency to CloudWatch.
    """
    metrics_payload = [{
        "MetricName": "Availability",
        "Dimensions": [{"Name": "TargetURL", "Value": target}],
        "Value": status_flag,
        "Unit": "Count"
    }]
    if latency_ms is not None:
        metrics_payload.append({
            "MetricName": "Latency",
            "Dimensions": [{"Name": "TargetURL", "Value": target}],
            "Value": latency_ms,
            "Unit": "Milliseconds"
        })
    cw_client.put_metric_data(
        Namespace=METRIC_NAMESPACE,
        MetricData=metrics_payload
    )

def handler(event, context):
    # Load monitored targets from JSON file packaged with Lambda
    targets_path = os.path.join(os.path.dirname(__file__), "targets.json")
    with open(targets_path, "r") as file:
        targets = json.load(file)

    run_summary = []
    for target in targets:
        status, latency = probe_url(target)
        push_metrics(target, status, latency)
        run_summary.append({"target": target, "status": status, "latency_ms": latency})

    print("Execution summary:", run_summary)
    return {
        "statusCode": 200,
        "body": run_summary
    }
