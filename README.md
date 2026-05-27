# KIRA AI-Ops GitOps Platform

## AI-Powered Kubernetes Observability & Incident Response Platform on AWS EKS

KIRA (Kubernetes Intelligent Reliability Assistant) is an AI-powered cloud-native DevOps platform designed to monitor, analyze, and troubleshoot Kubernetes workloads running on Amazon EKS.

The platform integrates Kubernetes, Prometheus, Grafana, GitOps workflows, PostgreSQL, and AI-driven operational analysis to simulate real-world Site Reliability Engineering (SRE) and AI-Ops practices.

---

## Features

- Kubernetes microservices deployment on AWS EKS
- GitOps-based Kubernetes management
- AI-powered cluster health analysis
- Incident detection and troubleshooting
- Prometheus monitoring stack
- Grafana observability dashboards
- Stateful PostgreSQL database deployment
- Kubernetes pod failure simulation
- Real-time operational insights
- Kubernetes troubleshooting workflows

---

## Tech Stack

- AWS EKS
- Kubernetes
- Docker
- Prometheus
- Grafana
- ArgoCD
- Python
- Streamlit
- PostgreSQL
- Helm
- GitHub Actions
- GitOps

---

## Architecture

```text
Users
   ↓
Frontend Microservices
   ↓
Kubernetes (AWS EKS)
   ↓
Prometheus Monitoring
   ↓
Grafana Dashboards
   ↓
KIRA AI Assistant
   ↓
Incident Analysis & Insights


---

## Project Structure

```text
boutique-microservices-aiops/
│
├── architecture/
├── docs/
├── screenshots/
├── backend/
├── frontend/
├── gitops/
├── kira-aiops/
├── monitoring/
├── k8s/
└── README.md


---

## Screenshots

### Grafana Dashboard

![Grafana Dashboard](screenshots/grafana-dashboard.png)

---

### Kubernetes Pods

![Kubernetes Pods](screenshots/kubernetes-pods.png)

---

### KIRA AI Assistant

![KIRA AI](screenshots/kira-ai.png)


---

## Deployment Steps

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/boutique-microservices-aiops.git