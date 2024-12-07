# Salvador, Gabriel 
# Pamplona, Gwyneth 

## Application Overview

The application stack consists of:
- **Django**: A Python web framework running with `gunicorn`.
- **PostgreSQL**: A database for storing application data.
- **NGINX**: A proxy server for routing incoming HTTP requests.

### Dependencies
- **Django**: Uses `psycopg-binary2` for PostgreSQL integration.
- **Gunicorn**: As the WSGI HTTP server.
- **PostgreSQL**: Backend database.
- **Docker**: For containerizing the application.
- **Kubernetes**: For orchestration.
- **Google Kubernetes Engine (GKE)**: As the Kubernetes provider.

---

## Deployment Architecture

### Pods
1. **django-app-deploy**: Contains the Django application container built from Docker.
2. **nginx-deployment**: Contains the NGINX container for proxying requests.
3. **postgres**: Contains the PostgreSQL container for database services.

### Services
1. **app-service**: Exposes necessary ports for the Django application.
2. **nginx-service**: Exposes ports for NGINX to handle HTTP traffic.
3. **postgres-service**: Exposes the PostgreSQL instance to the application.

### Ingress
- **network-loadbalancer**: Load balancer service for `nginx-service` to route incoming traffic.

### Autoscaling
- **Django Application**:  
  `kubectl autoscale deployment django-app-deploy --max 4 --min 1 --cpu-percent 1`
- **NGINX**:  
  `kubectl autoscale deployment nginx-deployment --max 4 --min 1 --cpu-percent 1`

### Storage Persistence
- **PostgreSQL**:
  - Persistent Volume: `postgres-pv`
  - Persistent Volume Claim: `postgres-pvc`
- **Django Static Files**:
  - Persistent Volume: `app-pv`
  - Persistent Volume Claim: `app-pvc`

---

## Deployment Process

### 1. Create Docker Image
Clone the GitHub repository and build the Docker image:
```bash
git clone <repository_url>
cd web
docker build -t <username>/<dockerhub_repo>:<tag> .
# Example:
docker build -t sampleuser/testrepo:latest .
docker push <username>/<dockerhub_repo>:<tag>
# Example:
docker push sampleuser/testrepo:latest
