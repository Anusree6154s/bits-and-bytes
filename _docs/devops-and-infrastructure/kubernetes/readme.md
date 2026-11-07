---
layout: default
title: Kubernetes
date: Nov 04, 2026
excerpt: Intro to kubernetes
parent: Devops And Infrastructure
permalink: kubernetes
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

## Linux Basics
Now some linux basics first so that we understand the working of K8s in comparison to physical servers much easily.

```
Data Center Rack
|-- Server 1
|    |-- CPU, RAM, SSD/HDD, Network Card
|    |--Linux Kernel
|    |--Processes running
|        |--nginx PID 101
|        |--postgers PID 220
|        |--node app PID 450
|-- Server 2
|-- Server 3
.
.
.
```

### Visualisation
```
Physical server

|-------------------|
| CPU --------------|-----> executes instructions
| RAM --------------|-----> process memory
| SSD/HDD ----------|-----> stores files/dbs/logs
| NIC/Network Card -|-----> sends and receives network packets
| --------------    |
| |Linux Kernel| ---|-----> schedules CPU time (sits between application
| --------------    |        and hardware)
|                   |       * manages memory
| Processes running:|       * manages file systems
| nginx PID 101     |       * manages networking via NIC
| postgres PID 220  |
| node app PID 450  |
|-------------------|
```

- **Process** = Program code + memory + CPU execution + kernel-managed resources 
- **Linux Kernel**
    - Sits between application and hardware
    - When app needs something, it initiates kernel and kernel initates disk for data
    - Eg: 
    ```
    node app
        |
        v
    Kernel sys call
        |
        v
    disk read
        |
        v
    SSD returns bytes
    ``` 
    - App never touches hardware directly. Kernel controls everything

### Visualising Process in RAM
```
RAM
|-----------------------|
| Process: nginx        |
|-----------------------|
| Process: postgres     |
|-----------------------|
| Process: nodes        |
|-----------------------|
| Linux Kernel Reserved |
|-----------------------|
```
- Each process getsisolated memory
- Kernel prevent process A from reading process B's memory

## Media Forge
I attempted learning more about linux and k8s with help of a partly done mini project. Techand their purposes:
- Docker: 
    - Run app in containers
    - SOlve issue of "works on my machine"
    - ALternatives:
        - Podman: docker compatible container engine
        - CXC/CXD: system containers
        - containerd
        - CRI-O
- Docker compose
    - Run multiple containers together (instead of running containers separately)
- kube ctl (pronounced: koobcuttle)
    - CLI to control k8 clusters
    - alternatives: Lens/Openlens UI, k9s, Rancher
- Kind (Full form: kubernetes in docker)
    - Runs local k8s cluster using docker containers
    - Lightweight alternatives to real k8 clusters
    - Alternative: Minikub, k3d, MicroK8s, Docker Desktop K8s 
- Helm
    - Package manager for K8s
    - npm for K8s
    - When lots of k8s yaml comes, helm ackages them into reusable templates called chartsw
    - ALternatives: Kustomize, Jsonnet/Tnaks, CUEe
- K9s
    - Terminal UI for k8s
    - Alternative to kubectl commands in terminal
    - ALternatives: OpenLens, Rancher, Octant
- OpenLens
    - Desktop GUI for k8s cluster
    - Alternatives: Lens, Rancher, Octant
- PNPM
    - Fullform: performative npm
    - Faster + efficient npm
    - Used for nx monorepos running multiple services
    - Alternative: npm, yarn, Bun package manager

## K8s Basics
So we are back to continuing with k8s basics dropping media forge in between 🥲🙂
### Linux Basics
Back to understanding linnux basics for k8s. THey include processes, ports, networking, DNS, file systems, permissions, env variables, systemd, services, logs

