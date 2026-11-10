---
layout: default
title: 08. K8s Leanring Continuation
date: Nov 10, 2026
excerpt: Intro to kubernetes (K8s learning continuation)
parent: Kubernetes
permalink: kubernetes-08-k8s-learning-continuation
---

# K8s learning (continuation)

- Linux namespaces
  - helps in isolation
  - types :- PID, NET, MNT, UTS, IPC, USER, CGROUP
- cgroups (control groups)
  - for resource control
  - tracks limits of resources
- Containerd - container runtime
- OCI (Open Container Initiative)
  - Container standards
  - defines standards for container image & container runtimes
  - Example :-
    - When we build an image, docker creates an OCI-compliant image
    - When we push it, and someone else pulls it, because it is OCI compliant, everyone follows it. The same image works across (docker, containerd, Podman, CRI-O, K8s, etc.)
- Istio vs port forwarding
  - port forwarding :-
    - Eg: kubectl port-forward svc/my-service 8080:80
    - temporary funnel from my-laptop to pod/svc
    - used for development / debugging / testing
    - Limitations :-
      - Only works while terminal session is running
      - not suitable for real cases
      - no public DNS, no production-grade traffic management, no SSL-TLS termination, no load balancing
    - Istio-ingress gateway :-
    - Expose app to internet permanently
    - Accepts traffic from users, browsers, mobile apps, APIs, etc.
    - Provides routing, TLS/HTTPS, traffic splitting, canary deployments, blue-green deployments, authentication/authorization, observability, rate limiting (w/ extensions)
    - Used when apps are deployed to a real environment like GKE, EKS, AKS, on-prem K8s, etc. Page 15(16)

## K8s visualisers

- K8s dashboard (legacy & deprecated)(GUI)
  - Steps
    - make sure you have helm installed and a running kind cluster. "helm version", "kubectl config current-context"
    - install K8s dashboard.

    ```
    "helm repo add kubernetes-dashboard kubernetes-retired.github.io/dashboard/"
    "helm repo update"
    "helm install kubernetes-dashboard \
        kubernetes-dashboard/kubernetes-dashboard \
      --namespace kubernetes-dashboard \
      --create-namespace"
    ```

    - verify installation : "kubectl get pods -n kubernetes-dashboard"
    - create admin account :-

    ```
    # dashboard-admin.yaml

    apiVersion: v1
    kind: ServiceAccount
    metadata:
        name: admin-user
        namespace: kubernetes-dashboard

    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
        name: admin-user

    roleRef:
        apiGroup: rbac.authorization.k8s.io
        kind: ClusterRole
        name: cluster-admin

    subjects:
        - kind: ServiceAccount
        name: admin-user
        namespace: kubernetes-dashboard
    ```

    - Apply this file "kubectl apply -f dashboard-admin.yaml"
    - Generate login token "kubectl -n kubernetes-dashboard create token admin-user"
    - Verify services "kubectl get svc -n kubernetes-dashboard"
    - portforward kong proxy :-

    ```
    "kubectl -n kubernetes-dashboard port-forward
    svc/kubernetes-dashboard-kong-proxy
    8443:443"
    ```

    - open https://localhost:8443 & login using token.
    - Every cluster and its associated details will be visible w/o any commands.

- Headlamp (GUI)
  - install as an app & open it ds.
  - clusters will already be there. 
- k9s (terminal GUI)
    - most used (it seems) 
- lens (GUI) - didn't try
