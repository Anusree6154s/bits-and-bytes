---
layout: default
title: 02. Media Forge
date: Nov 09, 2026
excerpt: Intro to kubernetes (Media Forge)
parent: Kubernetes
permalink: kubernetes-02-media-forge
---

## Media Forge

<p align='center'><img src='https://github.com/user-attachments/assets/4bd96a77-da9d-4b95-af9e-c9ca15b142f9' width=100/></p>

I attempted learning more about linux and k8s with help of a partly done mini project. Tech and their purposes:

- Docker:
  - Run app in containers
  - Solve issue of "works on my machine"
  - Alternatives:
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
  - Alternatives: Kustomize, Jsonnet/Tnaks, CUEe
- K9s
  - Terminal UI for k8s
  - Alternative to kubectl commands in terminal
  - Alternatives: OpenLens, Rancher, Octant
- OpenLens
  - Desktop GUI for k8s cluster
  - Alternatives: Lens, Rancher, Octant
- PNPM
  - Fullform: performative npm
  - Faster + efficient npm
  - Used for nx monorepos running multiple services
  - Alternative: npm, yarn, Bun package manager

