# Apply Deployment File
kubectl apply -f <deployment file>

# Architecture Diagram
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)

# Logging
kubectl describe pods <name-of-pod>
kubectl describe deployment <name-of-deployment>

# Trail logs
kubectl -n dev logs -f deployment/frontend-deployment --all-containers=true --since=10m 
kubectl logs --follow frontend-deployment-5cbd5bf884-7dfnp -n dev

kubectl create secret docker-registry my-registry-secret \
— docker-username=DOCKER_USER \
— docker-password=DOCKER_PASSWORD \
— docker-email=DOCKER_EMAIL

# Exposing a Service: https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/

kubectl expose deployment/frontend-deployment --type="NodePort" --port 8080 -n dev

export NODE_PORT="$(kubectl get services/frontend-deployment -n dev -o go-template='{{(index .spec.ports 0).nodePort}}')"

# port forwarding
# exposed port -> listening port
kubectl port-forward pod/frontend-deployment-7f449ff8fb-ntfqm 80:8080 -n dev
