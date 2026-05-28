report = """
# DevOps Incident Report

## Summary
Multiple DevOps failures detected.

## Failures Identified
- NPM dependency issue
- Terraform backend issue
- Docker registry issue
- Kubernetes pod failure

## Recommended Actions
- Reinstall npm dependencies
- Verify Terraform backend configuration
- Validate Docker credentials
- Check Kubernetes application logs

## Status
Investigation Completed Successfully
"""

with open("reports/incident-report.md", "w") as f:
    f.write(report)

print("Incident report generated successfully.")