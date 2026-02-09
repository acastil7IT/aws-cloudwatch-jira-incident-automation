# AWS CloudWatch and Jira Incident Automation

## Overview
This project demonstrates a basic cloud incident automation workflow using AWS and Jira. The purpose of the project is to show how monitoring tools can automatically create incident tickets when an issue occurs, instead of relying on manual reporting.

When an AWS Lambda function encounters errors, Amazon CloudWatch detects the issue and triggers an alarm. That alarm invokes a Lambda function which creates an incident in Jira. The incident then appears on a Jira board where it can be reviewed, tracked, and resolved.

---

## Tools Used
- AWS Lambda
- Amazon CloudWatch
- Jira (Free version)
- Python
- Jira REST API

---

## How the Workflow Functions
1. A Lambda function runs and encounters an error  
2. CloudWatch monitors Lambda error metrics  
3. A CloudWatch alarm is triggered when the error threshold is met  
4. The alarm invokes a Lambda function  
5. The Lambda function sends a request to the Jira REST API  
6. A new incident is created in Jira automatically  

---

## Jira Configuration
- Project name: **Cloud Operations**
- Board type: **Kanban**

Workflow states:
- To Do  
- In Progress  
- Done  

Each incident includes a summary, priority, labels, and a description indicating that the ticket was created automatically from an AWS alert.

---

## AWS Configuration
The Lambda function responsible for creating Jira incidents uses environment variables to store Jira credentials and configuration values securely. Authentication is handled using a Jira API token.

CloudWatch monitors Lambda error metrics and is configured with an alarm that invokes the Lambda function when errors occur.

---

## Testing Process
Testing was performed by intentionally triggering a Lambda error. CloudWatch detected the error, the alarm entered the ALARM state, and Jira incidents were created automatically. This confirmed that the monitoring and automation workflow functions as expected.

After testing was completed, the alarm was disabled to prevent additional incidents from being created.

---

## Project Structure
- `lambda_function.py` contains the Python code used by AWS Lambda
- Screenshots related to AWS and Jira are stored in a separate `screenshots` folder
- This README provides an overview of the setup and workflow

---

## Notes
This project focuses on understanding how cloud monitoring, alerting, and ticketing systems work together. It is designed to be simple, readable, and easy to follow while reflecting real-world operational behavior.
