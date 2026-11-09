---
layout: default
title: 05. K8s Cluster Diagram
date: Nov 09, 2026
excerpt: Intro to kubernetes (K8s Cluster Diagram)
parent: Kubernetes
permalink: kubernetes-05-k8s-cluster-diagram
---

## K8s Cluster Diagram (For Reference)

### k8s clusters

```
Cluster 1 (ex: prod cluster)
|---*Control Plane node A*
|    |---kube-apiserver
|    |    ↳ Authentication
|    |    ↳ Authorization (RBAC)
|    |    ↳ Admission controllers
|    |    ↳ API endpoints
|    |    ↳ Validation
|    |    ↳ watches
|    |---etcd
|    |     ↳ deployments
|    |     ↳ replicasets
|    |     ↳ pods
|    |     ↳ services
|    |     ↳ configmaps
|    |     ↳ secrets
|    |     ↳ namespaces
|    |     ↳ service accounts
|    |     ↳ roles
|    |     ↳ rolebindings
|    |     ↳ clusterroles
|    |     ↳ clusterrolebindings
|    |     ↳ jobs
|    |     ↳ cronjobs
|    |     ↳ daemonsets
|    |     ↳ statefulsets
|    |     ↳ persistent volumes
|    |     ↳ persistent volume claims
|    |     ↳ storage classes
|    |     ↳ nodes
|    |     ↳ events
|    |     ↳ leases
|    |     ↳ Custom Resources (CRD)
|    |---Kubernetes Controller Manager
|    |     ↳ deployment controller (creates/manages replicasets)
|    |     ↳ replicaset controller (creates/deletes pods)
|    |     ↳ job controller
|    |     ↳ cronjob controller
|    |     ↳ statefulset controller
|    |     ↳ daemonset controller
|    |     ↳ namespace controller
|    |     ↳ node controller
|    |     ↳ service account controller
|    |     ↳ endpoint slice controller
|    |     ↳ persistent volume controller
|    |     ↳ replication controller
|    |     ↳ ... many other controllers.
|    |--- kube-scheduler
|    |      ↳ watches pending pods
|    |      ↳ selects worker node
|    |      ↳ resource calculations
|    |      ↳ affinity rules
|    |      ↳ taints & tolerations
|    |      ↳ writes node assignment
|    |---Other controller managers (optional)
|          ↳ load balancer controller
|          ↳ route controller
|          ↳ volume controller
|          ↳ node-controller
|---*Control Plane node B*
|      ↳ ... same as above
↳ Cluster 2 (ex: staging cluster)



Developer machine / CI server
↳ kubectl
↳ kube-adm
↳ Helm
↳ Kustomize
↳ ArgoCD
↳ Terraform
↳ Custom clients

Worker Nodes
↳ Node 1
|  ↳ kubelet
|  |  ↳ talks to api server
|  |  ↳ watches Pod objects
|  |  ↳ starts containers
|  ↳ Container runtime
|  |  ↳ containerd
|  |  ↳ CRI-O
|  |  ↳(formerly docker)
|  ↳ kube-proxy
|  |  ↳ Service Networking
|  |  ↳ iptables
|  |  ↳ IPVS
|  ↳ Running Pods
|    ↳ Pod A
|    ↳ Pod B
|    ↳ Pod C
↳ Node B -> Same structure
↳ Node C -> Same structure
```
