

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
- Email alert
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

## Quick Runbook

**Purpose:**  
This runbook provides the essential steps to operate, check, and maintain the NetWatch Agent monitoring system.

---

### 1. Deploy the Stack
From the project root (where `app.py` is located):

```powershell
.venv\Scripts\activate
cdk deploy
```
Confirm the deployment when prompted.

---

### 2. Update Monitored Sites
1. Open `lambda\targets.json`.
2. Add or remove URLs (must include `https://`).
3. Save the file.
4. Redeploy with:
   ```powershell
   cdk deploy
   ```

---

### 3. Check Lambda Execution
- Go to **AWS Console → Lambda → SiteProbeLambda** (or your function name).
- View **Monitor → Logs** to see recent runs.
- Use **Test** to trigger manually.

---

### 4. View Metrics & Dashboard
- **CloudWatch → Metrics → NetWatchMetrics**  
  - *Availability*: 1 = up, 0 = down  
  - *Latency*: Response time in milliseconds
- **CloudWatch → Dashboards → NetWatchMetrics** for graphs.

---

### 5. Troubleshooting
| Issue | Action |
|-------|--------|
| No metrics in CloudWatch | Check Lambda logs for errors, confirm URLs are valid |
| Lambda timeout | Increase timeout in `netwatch_agent_stack.py` |
| Permission errors | Ensure Lambda role has `cloudwatch:PutMetricData` |

---

### 6. Maintenance
- **Add/remove sites**: Edit `targets.json` and redeploy.
- **Change schedule**: Update EventBridge rule in `netwatch_agent_stack.py`.
- **Update dependencies**:  
  ```powershell
  pip install -r requirements.txt --upgrade
  ```

---
### 7. Some output screenshots
- using the command cdk bootstrap
<img width="1144" height="617" alt="image" src="https://github.com/user-attachments/assets/b5f4af8a-1721-49df-a8cc-a5c09a429818" />
-using the command cdk synth
<img width="1121" height="618" alt="image" src="https://github.com/user-attachments/assets/84db450d-0dbe-4b7b-b211-242be3f6bce1" />
-using the command deploy
<img width="1121" height="631" alt="image" src="https://github.com/user-attachments/assets/f6cf4e23-116f-4ee3-8f51-486ee0d964b4" />

-After deploying is sucessfull we go to our aws console and we can see like below image:
<img width="1102" height="549" alt="image" src="https://github.com/user-attachments/assets/c4fbc57c-b32d-4360-86c9-e8554e566901" />
after that we have to click on the function and test it and if it get sucess it shows like this:
<img width="1085" height="555" alt="image" src="https://github.com/user-attachments/assets/ad24f905-c31f-4357-82df-5a208436e54f" />
<img width="1065" height="573" alt="image" src="https://github.com/user-attachments/assets/3cfa3c28-3fd2-4d16-bd0d-ac4bd3e6a394" />
- Using the command destroy :
  <img width="1134" height="631" alt="image" src="https://github.com/user-attachments/assets/e10781d8-5b16-4e71-add8-0251ce04796d" />

-Deploy command 
<img width="1221" height="631" alt="image" src="https://github.com/user-attachments/assets/5f901f4a-25e1-479e-bf4a-218d60fed8c9" />

<img width="1295" height="638" alt="image" src="https://github.com/user-attachments/assets/b4bad63e-1386-4dc1-8730-8a5a5a434663" />

- result in aws after deploy
  <img width="1332" height="552" alt="image" src="https://github.com/user-attachments/assets/6952a0c6-d90c-47e1-a39e-48d14f10dc1b" />


-SNS alert
<img width="1339" height="582" alt="image" src="https://github.com/user-attachments/assets/1ee59780-6550-4c93-a786-68fd0797e65c" />

-Email alert
<img width="1293" height="598" alt="image" src="https://github.com/user-attachments/assets/6f0a373b-65c9-402e-9c1c-7319fe88c8ee" />

-Dynamo db table
<img width="1343" height="605" alt="image" src="https://github.com/user-attachments/assets/d3b76bc1-7c4c-4408-b794-ce99db05b22e" />




