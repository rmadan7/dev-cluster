#!/bin/bash

# re-build frontend-deployment
docker build -t frontend-dev:latest .

# rolling update to the deployment
kubectl set image deployments/frontend-deployment myapp=frontend-dev:latest -n dev