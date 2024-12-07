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
- **network-ingress**: Ingress for load balancer service

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
Clone the GitHub repository, and build and push the Docker image:
```bash
git clone <repository_url>
cd web
docker build -t <username>/<dockerhub_repo>:<tag> .
# Example:
docker build -t sampleuser/testrepo:latest .
docker push <username>/<dockerhub_repo>:<tag>
# Example:
docker push sampleuser/testrepo:latest
```
### 2. Create GKE Cluster
Create Google Kubernetes Engine Cluster through Google Cloud Shell:
```bash
# Run the following in Google Cloud Shell:

export my_zone=<ZONE>  # Example: asia-east2-a
export my_cluster=<CLUSTER_NAME>  # Example: my_cluster

gcloud container clusters create $my_cluster \
  --num-nodes 3 \
  --zone $my_zone \
  --enable-ip-alias
```
### 3. Apply Kubernetes Manifests
Clone the GitHub repository, and apply the manifests:
```bash
# Run the following in Google Cloud Shell:

export my_zone=<ZONE>  # Example: asia-east2-a
export my_cluster=<CLUSTER_NAME>  # Example: my_cluster

git clone <repository_url>
kubectl apply -f kubernetes-manifests/app
kubectl apply -f kubernetes-manifests/db
kubectl apply -f kubernetes-manifests/network
kubectl apply -f kubernetes-manifests/nginx
```

### 4. Reserve External IPs for Load Balancer and Ingress

1. Navigate to Google Cloud Console > VPC > IP Address > Reserve External IP-Address.

2. Reserve:
    1st IP: Regional (for load balancer).
    2nd IP: Global (for ingress).

3. Update loadBalancerIP in your manifests to reflect the reserved IPs:
``` yaml
apiVersion: v1
kind: Service
metadata:
  name: network-loadbalancer
spec:
  type: LoadBalancer
  loadBalancerIP: [XX.XX.XX.XX] # Replace this
  selector:
    name: nginx-deployment
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

### 5. Create Django Superuser

To create a Django superuser for the admin interface:
```bash
kubectl get pods
kubectl exec -it <django-app-pod-name> -- /bin/bash
/opt/venv/bin/python manage.py createsuperuser
```