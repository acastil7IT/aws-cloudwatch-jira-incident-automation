import json
import os
import base64
import urllib.request
import urllib.error


def adf_paragraph(text: str) -> dict:
   """Build a simple Atlassian Document Format (ADF) description."""
   return {
       "type": "doc",
       "version": 1,
       "content": [
           {
               "type": "paragraph",
               "content": [{"type": "text", "text": text}]
           }
       ]
   }


def lambda_handler(event, context):
   jira_base = os.environ["JIRA_BASE_URL"].rstrip("/")
   jira_email = os.environ["JIRA_EMAIL"]
   jira_token = os.environ["JIRA_API_TOKEN"]
   project_key = os.environ["JIRA_PROJECT_KEY"]
   issue_type = os.environ.get("JIRA_ISSUE_TYPE", "Task")


   auth_b64 = base64.b64encode(f"{jira_email}:{jira_token}".encode()).decode()


   # Build a clean incident-style description
   description_text = (
       "Incident Type: Cloud Monitoring Alert\n\n"
       "Trigger:\n"
       "- Manual Lambda test\n\n"
       "Source:\n"
       "- AWS Lambda (automated)\n\n"
       "Raw Event:\n"
       f"{json.dumps(event)}"
   )


   payload = {
       "fields": {
           "project": {"key": project_key},
           "summary": "[Cloud Alert] Lambda error rate high",
           "description": adf_paragraph(description_text),
           "issuetype": {"name": issue_type},
           "priority": {"name": "High"},
           "labels": ["aws", "lambda", "cloudwatch", "automation", "incident"]
       }
   }


   req = urllib.request.Request(
       url=f"{jira_base}/rest/api/3/issue",
       data=json.dumps(payload).encode("utf-8"),
       headers={
           "Authorization": f"Basic {auth_b64}",
           "Accept": "application/json",
           "Content-Type": "application/json"
       },
       method="POST"
   )


   try:
       with urllib.request.urlopen(req, timeout=15) as res:
           body = res.read().decode("utf-8")
           return {"statusCode": res.status, "body": body}
   except urllib.error.HTTPError as e:
       return {"statusCode": e.code, "body": e.read().decode("utf-8")}
   except Exception as e:
       return {"statusCode": 500, "body": str(e)}



