# Deployment Runbook for SIEM Platform

## Overview

This document serves as a deployment runbook for the SIEM (Security Information and Event Management) platform. It outlines the steps required to deploy the system in various environments, including local, staging, and production.

## Prerequisites

Before deploying the SIEM platform, ensure that the following prerequisites are met:

- A compatible version of Python (3.8 or higher)
- Docker and Docker Compose installed
- Access to a Kubernetes cluster (for Kubernetes deployments)
- Access to a cloud provider (for cloud deployments)
- Required configurations in the `configs` directory

## Deployment Steps

### Local Deployment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/siem-platform.git
   cd siem-platform
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Docker Compose**
   ```bash
   cd infra/docker
   docker-compose up -d
   ```

4. **Verify Services**
   Ensure that all services are running correctly by checking the logs:
   ```bash
   docker-compose logs
   ```

### Kubernetes Deployment

1. **Configure Kubernetes Context**
   Ensure your `kubectl` is configured to point to the correct cluster.

2. **Deploy Using Helm**
   ```bash
   cd infra/helm/siem-chart
   helm install siem-platform .
   ```

3. **Verify Deployment**
   Check the status of the deployment:
   ```bash
   kubectl get pods
   ```

### Cloud Deployment

1. **Configure Terraform**
   Update the Terraform configuration files in `infra/terraform/cloud` with your cloud provider credentials and settings.

2. **Initialize Terraform**
   ```bash
   cd infra/terraform/cloud
   terraform init
   ```

3. **Apply Terraform Configuration**
   ```bash
   terraform apply
   ```

4. **Verify Resources**
   Check the cloud provider's dashboard to ensure resources are created successfully.

## Post-Deployment

- **Access the Web Dashboard**
  The web dashboard can be accessed at `http://localhost:3000` (for local deployment) or the respective URL for cloud/Kubernetes deployments.

- **Monitor Logs**
  Use the configured logging tools (e.g., Prometheus, Loki) to monitor the logs and performance of the SIEM platform.

## Troubleshooting

- **Common Issues**
  - If services fail to start, check the logs for errors.
  - Ensure that all environment variables are set correctly in the configuration files.

- **Support**
  For further assistance, refer to the `docs/ONCALL_PLAYBOOK.md` for emergency intervention procedures.

## Conclusion

This runbook provides a comprehensive guide to deploying the SIEM platform across different environments. Follow the steps carefully to ensure a successful deployment.