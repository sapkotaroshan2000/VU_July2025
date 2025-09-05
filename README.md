Alright Roshan — here’s a **clear, human‑readable README** for your project that’s simple enough for a new user to follow, but still meets the **rubric expectations** for clarity, installation/use instructions, and professionalism.  
I’ve kept it **original**, avoided filler or AI‑style fluff, and made sure it’s easy to follow while covering the essentials.

---

# NetWatch Agent – Website Monitoring with AWS CDK

## Overview
NetWatch Agent is a cloud‑based monitoring tool that checks the availability and response time of multiple websites.  
It runs automatically on a schedule using AWS Lambda and EventBridge, and sends custom metrics to Amazon CloudWatch for real‑time tracking.

The system includes:
- **Automated checks** for multiple URLs
- **Custom CloudWatch metrics**: Availability (up/down) and Latency (milliseconds)
- **Dashboard** for visualising results
- **Configurable site list** without changing code

---

## Features
- Monitors any number of websites you define in a JSON file
- Runs every 5 minutes by default
- Stores metrics in a dedicated CloudWatch namespace
- Displays results in a CloudWatch dashboard
- Works with Python 3.13 Lambda runtime

---

## Prerequisites
Before you start, make sure you have:
- **AWS account** with permissions to deploy CDK stacks
- **AWS CLI** installed and configured (`aws configure`)
- **AWS CDK v2** installed (`npm install -g aws-cdk`)
- **Python 3.13** installed
- **Virtual environment** set up for the project

---

## Installation

1. **Clone the repository**  
   ```powershell
   git clone <your-repo-url>
   cd netwatch_agent
   ```

2. **Create and activate a virtual environment** (Windows PowerShell)  
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```powershell
   pip install -r requirements.txt
   ```

4. **Bootstrap CDK** (only needed once per AWS account/region)  
   ```powershell
   cdk bootstrap
   ```

---

## Configuration

1. **Edit the monitored sites list**  
   Open `lambda\targets.json` and add or remove URLs:
   ```json
   [
       "https://www.example.com",
       "https://www.github.com",
       "https://www.python.org"
   ]
   ```

2. **Adjust schedule (optional)**  
   The default schedule is every 5 minutes.  
   To change it, edit the EventBridge rule in `netwatch_agent_stack.py`.

---

## Deployment

From the project root (where `app.py` is located):

```powershell
.venv\Scripts\activate
cdk deploy
```

When prompted, confirm the deployment.

---

## Usage

- The Lambda function will run automatically on the schedule you set.
- To run it manually:
  1. Go to the AWS Lambda console.
  2. Select your function.
  3. Click **Test**.

- View metrics:
  - **CloudWatch → Metrics → NetWatchMetrics**
  - **CloudWatch → Dashboards → NetWatchMetrics**

---

## Troubleshooting

- **No metrics showing**:  
  - Check CloudWatch Logs for errors.
  - Ensure `targets.json` is deployed with the Lambda code.
  - Confirm IAM permissions include `cloudwatch:PutMetricData`.

- **Lambda errors**:  
  - Verify all URLs in `targets.json` are valid and include `https://`.
  - Check that Python dependencies are compatible with Lambda runtime.

---

## Maintenance

- To add/remove monitored sites:  
  Edit `targets.json` and redeploy with `cdk deploy`.

- To change runtime or memory:  
  Update the Lambda configuration in `netwatch_agent_stack.py`.

---

## Ethical & Privacy Considerations
- Only monitor websites you own or have permission to check.
- Avoid sending sensitive data in metrics or logs.
- Follow AWS best practices for IAM permissions.

---


If you want, I can also prepare a **short “Runbook” section** for quick operational reference, which would help you score higher in the *Project Documentation* part of the rubric.  
Do you want me to add that?
