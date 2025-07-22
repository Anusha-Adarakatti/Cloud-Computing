# Issue Tracking Application with Kubernetes

![Kubernetes](https://img.shields.io/badge/kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

A microservice-based issue tracking system with:
- User interface for submitting issues
- Admin dashboard for viewing issues
- PostgreSQL database
- Kubernetes deployment with Horizontal Pod Autoscaling (HPA)

## Architecture
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ User │ │ Admin │ │ │
│ Service │─────│ Service │─────│ PostgreSQL │
│ (Flask) │ │ (Flask) │ │ │
└─────────────┘ └─────────────┘ └─────────────┘


## Features

- **User Service**: Web interface for submitting support tickets
- **Admin Service**: Dashboard to view all submitted issues
- **Automatic Scaling**: HPA automatically scales pods based on CPU usage
- **Persistent Storage**: PostgreSQL database for issue storage

## Prerequisites

- Minikube ([installation guide](https://minikube.sigs.k8s.io/docs/start/))
- kubectl ([installation guide](https://kubernetes.io/docs/tasks/tools/))
- Docker ([installation guide](https://docs.docker.com/get-docker/))

## Quick Start

### 1. Start Minikube
```bash
minikube start --driver=docker
minikube addons enable metrics-server
eval $(minikube docker-env)
docker build -t user-service:local ./user_service
docker build -t admin-service:local ./admin_service
kubectl apply -f k8s/postgres.yaml
kubectl apply -f k8s/user-app.yaml
kubectl apply -f k8s/admin-app.yaml
kubectl get pods
kubectl get hpa

open two terminal in git bash and run this 
minikube service user-service    # Opens user interface in browser
minikube service admin-service   # Opens admin dashboard in browser

#To stop
kubectl delete -f k8s/
minikube stop
