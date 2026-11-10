---
layout: default
title: 07. K8s Next Topics
date: Nov 10, 2026
excerpt: Intro to kubernetes (K8s next topics)
parent: Kubernetes
permalink: kubernetes-07-k8s-next-topics
---

## Next topics in k8s

- Metric server
- HPA
- Deployment replicas

### Metrics server :-

- shows metrics for pods & nodes for resource usage 
- Steps :- first install metrics-server from repository, then update metric-server with starter flag. check metrics
  "kubectl top nodes",
  "kubectl top pods -n media-forge-dev"

> **Importance**
> HPA reads metrics from metrics - server to decide autoscaling. 

### HPA
- Write an hpa.yaml with threshold mentioned, beyond which if cpu usage goes, then it increases replicas.

## Common K8s commands
- kind create cluster --name <random-cluster-name> --config <config-path>
- in config file:
```
kind: cluster
apiVersion:  kind.x-k8s.io/v1alpha4
nodes:
    - role: control-plane
    - role: worker ...etc
```
- kind get clusters (see clusters created)
- kubectl get clusters (see clusters configured)
- kubectl config get-contexts (see multiple cluster contexts)
- docker build -t <random-tag-name> -f Dockerfile <path-to-dockerfile> (to build image from code changes)
- kind load docker-image <tag-name> --name <cluster-name>
- kubectl apply -k <path-to-file|-kustomization> (to start related pods & clusters. apply kustomization file for each. path you want to spin. eg: for each service)   