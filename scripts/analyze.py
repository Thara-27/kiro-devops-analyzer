import os

log_folder = "logs"

print("\n===== AI DEVOPS FAILURE ANALYZER =====\n")

for file in os.listdir(log_folder):

    path = os.path.join(log_folder, file)

    with open(path, "r") as f:
        logs = f.read()

    print(f"\nAnalyzing: {file}\n")

    # GitHub / NPM
    if "dependency conflict" in logs:
        print("Category: NPM Dependency Failure")
        print("Severity: HIGH")
        print("Root Cause: Dependency version conflict")
        print("Suggested Fix:")
        print("Delete package-lock.json and run npm install\n")

    # Terraform
    elif "terraform init failed" in logs:
        print("Category: Terraform Failure")
        print("Severity: HIGH")
        print("Root Cause: Backend initialization issue")
        print("Suggested Fix:")
        print("Verify Terraform backend configuration\n")

    # Docker
    elif "docker build failed" in logs:
        print("Category: Docker Build Failure")
        print("Severity: MEDIUM")
        print("Root Cause: Docker registry access denied")
        print("Suggested Fix:")
        print("Verify DockerHub credentials\n")

    # Kubernetes
    elif "CrashLoopBackOff" in logs:
        print("Category: Kubernetes Failure")
        print("Severity: HIGH")
        print("Root Cause: Container crashing repeatedly")
        print("Suggested Fix:")
        print("Check application startup logs\n")

    else:
        print("Unknown issue detected\n")