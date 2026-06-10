Project Name: flask-multi-k8s

Multi‑Container Flask API + PostgreSQL + Docker Compose + Kubernetes Project

## OBJECTIVE

- Build a multi‑container, cloud‑ready application using:

- Python Flask API

- PostgreSQL database

- Docker & Docker Compose

- Kubernetes (Deployments, Services, PVC, ConfigMaps, Secrets, Ingress)

- Cloud‑ready container images (Docker Hub / ACR)

- Optional deployment to Azure Kubernetes Service (AKS)

This project teaches the full DevOps lifecycle: containerization → orchestration → routing → cloud deployment.

## PROJECT DESCRIPTION
This project is a clean, real, Kubernetes‑ready multi‑container application designed to simulate a real microservice deployment.

It includes:

- A Flask REST API

- A PostgreSQL database with initialization SQL

- A Docker Compose setup for local multi‑container development

- Kubernetes manifests for production‑style orchestration

- Persistent storage using PVC

- Ingress routing using NGINX

- Docker Hub image publishing

Optional AKS deployment

You learn how to:

---> Build and tag images

---> Run multi‑container apps locally

---> Scale services

--> Use Kubernetes networking

--> Store secrets/configs

--> Expose services with Ingress

--> Deploy to the cloud

## FEATURES

### Flask API

- / — root endpoint

- /health — health check

- /db — database connectivity test

### PostgreSQL Database

- Runs as its own container/pod

- Credentials stored in Secrets

- Initialization SQL via init.sql

- Persistent storage via PVC

### Docker Compose

- Runs API + DB locally with one command

- Shared network

- Environment variable injection

### Kubernetes

- Deployments for API + DB

- ClusterIP Services

- Secrets + ConfigMaps

- PersistentVolumeClaim for DB

- Ingress routing

- Horizontal scaling

### Cloud‑Ready

- Docker Hub image

- ACR import

- AKS deployment support

## Project Structure

app/

    app.py

    Dockerfile

    requirements.txt
  

db/

  init.sql
  

k8s/

    api-deployment.yaml

    api-service.yaml

    configmap.yaml

    db-deployment.yaml

    db-service.yaml

    pvc.yaml

    secret.yaml


docker-compose.yaml

.gitignore

README.md

## FILE BREAKDOWN

app/app.py

- Flask application

- Defines API routes

- Connects to PostgreSQL

app/requirements.txt

- Python dependencies

app/Dockerfile

- Builds the Flask API image

db/init.sql

- SQL script executed on first DB startup

- Creates tables or seeds initial data

docker-compose.yaml

- Defines the local multi‑container environment:

- Flask API container

- PostgreSQL container

- Shared network

- Environment variables

- Port mappings

Run everything locally with:

--> docker compose up --build

## Kubernetes Manifests (k8s/)

api-deployment.yaml

- Deployment for Flask API

- Uses Docker Hub image

- Replicas for scaling

api-service.yaml

- ClusterIP service for internal routing

db-deployment.yaml

- Deployment for PostgreSQL

- Mounts PVC for persistence

- Uses ConfigMap + Secret

db-service.yaml

- ClusterIP service for DB access

pvc.yaml

- PersistentVolumeClaim for PostgreSQL data

configmap.yaml

- Non‑sensitive DB config

secret.yaml

- Base64‑encoded DB credentials

## How to Run the Project 

# DOCKER SIDE 

1- Run Locally with Docker Compose

--> docker compose up --build

Test API

--> http://localhost:5000

Output: {"message": "Flask API running in a multi-container setup"}

Test DB:

--> http://localhost:5000/db

Output: {"database_time": "2026-06-07T05:13:22.123456"}

Health endpoint

--> http://localhost:5000/health

Output: {"status": "ok"}

# KUBERNETES SIDE

2- Build Docker Image for Kubernetes

Start the cluster 

--> minikube start

Build Docker Image using minikube 

--> minikube image build -t flask-k8s-lab:v1 ./app

3- Apply the manifests (in the correct order)

- ConfigMap + Secret
  
bash

--> kubectl apply -f k8s/configmap.yaml

--> kubectl apply -f k8s/secret.yaml

- PersistentVolumeClaim

bash

--> kubectl apply -f k8s/pvc.yaml

- Database Deployment + Service
  
bash

--> kubectl apply -f k8s/db-deployment.yaml

--> kubectl apply -f k8s/db-service.yaml

- API Deployment + Service
  
bash

--> kubectl apply -f k8s/api-deployment.yaml

--> kubectl apply -f k8s/api-service.yaml


3- Verify everything is running 

Check pods:

bash

--> kubectl get pods

Output:

flask-api-xxxxx       Running

flask-api-yyyyy       Running

postgres-xxxxx        Running


Check services:

bash

--> kubectl get svc

Output:

flask-api   ClusterIP   5000/TCP

postgres    ClusterIP   5432/TCP


Check PVC:

bash

---> kubectl get pvc

Output:

postgres-pvc   Bound

This means your database has persistent storage.


4- Access the Flask API (local cluster)

Since the API Service is ClusterIP, it’s internal only.

To access it, we use port‑forwarding:

bash

--> kubectl port-forward deployment/flask-api 5000:5000

Now open:

--> http://localhost:5000/

--> http://localhost:5000/health

--> http://localhost:5000/db

If /db returns a timestamp, your API successfully connected to PostgreSQL inside Kubernetes.

7- Scale the API 

bash

--> kubectl scale deployment flask-api --replicas=5

Check pods again:

bash

--> kubectl get pods

Output: You’ll see 5 API pods running.

This is horizontal scaling — the core of Kubernetes.


---------------------------------------------------------------------------

## STOP: THIS IS WHERE YOU FINISH RUNNING KUBERNETES LOCALLY

From now on, you are starting to push the image to registry in Azure

----------------------------------------------------------------------------



-----------------------------------------------------------
3- Push Image to Docker Hub

--> docker tag flask-k8s-lab:v1 YOURNAME/flask-k8s-lab:v1

--> docker push YOURNAME/flask-k8s-lab:v1

Update Deployment:

  image: YOURNAME/flask-k8s-lab:v1


4- Deploy to Kubernetes

-->kubectl apply -f k8s/

Check pods

--> kubectl get pods


5- Enable Ingress (Minikube)

-->minikube addons enable ingress
  
Add host entry:

--> <MINIKUBE_IP>   flask.local

Access:

--> http://flask.local/
