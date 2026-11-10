---
layout: default
title: 06. K8s Points to Remember
date: Nov 10, 2026
excerpt: Intro to kubernetes (K8s Points to Remember)
parent: Kubernetes
permalink: kubernetes-06-k8s-points-to-remember
---

## K8s app (points to remember)

- using kind locally
- we create a control plane node from a docker container.
- In kind we schedule pods & system related pods both in control plane node. [No taint. In general deployment platforms like GKE, EKS, etc. taints control plane node as "noschedule" to avoid schedule of worker nodes]
- Commands to apply yamls `kubectl apply -f <file-path>`
- command to read applied yamls `kubectl get all`, `kubectl get pods`, `kubectl get services`, ..etc
- Each time you update yaml, you need to `kubectl apply -f filename` & then `kubectl rollback restart deployment <service-name>`
- Everytime you change any code file we need to `nx build <service-name>`, `docker build t <tag-name> -f <dockerfile-path>`, `kind load docker-image <tag-name> --name <control-plane-cluster-name>`
- Kustomize config:-
  - Base files are template files.
  - Any config in overlay file overrides settings in base file (eg: overlay namespace overrides base namespace).
- "kind" is local K8s setup. "kubectl" is cli client to communicate of either kind or GKE or cloud K8s.
- "Kustomize" is part of kubectl cli
- Steps to deploy a micro service to local K8s
  1.  make sure all rotates mentioned in deployment.yaml readiness & liveness probe exists. (Health api)
  2.  Create Dockerfile.tar is in the target microservice file.
      - Eg:
      ```
      From node:22-alpine
      WORKDIR /app
      copy package.json pnpm-lock.yaml
      RUN corepack enable
      RUN pnpm install --ignore-scripts
      copy apps/auth-service/dist
      CMD ["node", "main.js"]`
      ```
  3.  Build image -> `docker build -t <tag-name> -f <path-to-Dockerfile> . --no-cache `
  4.  Load into kind cluster `kind load docker-image <tag-name> --name=<cluster-name>`
  5.  Apply new yaml files or restart existing deployment.
  - apply -> `kubectl apply -k <path-to-overlays>` (via Kustomize for all files)
  - restart -> `kubectl rollout restart deployment <service-name> -n <name-space>`
  6. Expose ingress port for calling apis:-
    - "kubectl port-forward -n <ingress-service-name> service/ingress-nginx-controller 8080:80" 
    > To check logs: "kubectl logs deployment/media-service -n <name-space>" 
    > Verify images loaded in kind:  "docker exec <control-plane-node-name> crictl images"

