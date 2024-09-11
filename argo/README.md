kubectl create ns argocd

u: admin
p: kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 --decode ; echo

helm
------------------------------
helm repo add argo https://argoproj.github.io/argo-helm
helm search repo argo



References:
https://devopscube.com/setup-argo-cd-using-helm/