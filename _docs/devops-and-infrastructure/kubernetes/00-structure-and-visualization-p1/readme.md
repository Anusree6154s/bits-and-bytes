---
layout: default
title: 00. Structure and Visualisation
date: Nov 04, 2026
excerpt: Intro to kubernetes - 00. Structure and Visualisation
parent: Kubernetes
permalink: kubernetes-00-structure-and-visualization
---
# Kubernetes (K8s)

<p align='center'><img src='https://github.com/user-attachments/assets/f0cac749-5d43-4a25-8865-da9bd83f2e87' width=100/></p>

## Structure and visualisation

Let us visualise it as a rack of physical servers

### Visualisation

```
Datacenter Rack
|--Physical Servers
```

Eg:

```
Datacenter Rack
|--Server A
|    |--Control Plane (Management brain)
|        |--Api Server
|        |--Scheduler
|        |--Control Manager
|        |--etcd
|--Server B
|    |--kubelet (local node employee/node agent)
|    |--container runtime (executes runtime)
|    |--Pods (workloads)
|        |--Pod
|        |   |--Container (nestJS)
|        |--Pod
|            |--Container (Redis)
|--Server C (worker node)
|   |--kubelet
|   |--Container runtime
|   |--Pods
|        |--Pod
|            |--Container (Postgres)
|--Server D (worker node)
    |--kubelet
    |--container runtime
    |--Pods
        |--Pod
            |--Container (Prometheus)
```

[Continued in [here](/kubernetes-04-k8s-structure-and-visualization)]

