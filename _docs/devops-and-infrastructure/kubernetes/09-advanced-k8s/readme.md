---
layout: default
title: 09. Advanced K8s
date: Nov 11, 2026
excerpt: Intro to kubernetes (Advanced K8s)
parent: Kubernetes
permalink: kubernetes-09-advanced-k8s
---

# Advanced K8s (Story Based)

```
Devops
|-- K8s
    |-- K8s Fundamentals
    |-- Application packaging
    |    |-- helm
    |    |-- charts
    |    |-- values.yaml
    |    |-- chart.yaml
    |    |-- helm repositories
    |-- Gitops
    |    |-- Argo CD
    |    |-- Applications
    |    |-- Application sets
    |    |-- SyncReconciliation
    |    |-- Drift detection
    |    |-- Git as source of truth
    |-- Continuous delivery (CD)
        |-- Progressive Delivery
        |-- Rollbacks
        |-- Automated deployments
```

- Without helm
  - Suppose you have multiple services like frontend, backend, postgres, redis, ingress, etc. For each one will have to write deployment.yaml, service.yaml, ingress.yaml, configmap.yaml, secret.yaml, pvc.yaml, etc.
  - This results in 20, 30, 50 yamls... For deploying in different environments like dev & prod we will have to copy that files multiple times.
  - Too much work, duplicate files.
- With helm
  - Reduced duplication via templates
  - Thus, it is most useful when used in combination w/ template expressions like `{{values.xyz.yz}}` But one can run "helm install myapp" without template expressions just with static data though it is same.(Running above mentioned command is called as installing a helm chart or installing a release.)
  - Template files (with template expressions) are called value files
- Value files
  - To deploy different kinds of values to different environments (Eg: values-dev.yaml)
  - Avoid duplicated manifests while still maintaining operationBinding to k8s env file, but w/o security.
- Charts.yaml
  - Addition of it to any folder makes that folder a valid "chart" & makes helm recognise it as one installable package.
  - Running "helm install myrelease my-app" (Installing a helm chart / release)
  - In general, we don't push charts (folder created w/ charts.yaml) into OCI registries (open w/ charts.yaml) into OCI registries (open w/ charts.yaml). It is just spun on the repos required nodes.
  - But in general, we push to OCI registries same as docker images (Eg: dockerhub, github container registry, Amazon ECR, Google artifact registry, Azure container registry).
- Multiple charts
  - by having multiple folders ref chart.yaml to install.
- Third party charts
  - to install, popular reusable packages/charts like prometheus, grafana, etc. redis, postgres, etc.
  - Installing multiple helm charts
    - Helm file
      - used for describing multiple helm releases in one place, or deploying them together & volatile controlling, ordering & shared configuration.
- Gitops / ArgoCD
  - Subset of DevOps.
  - Focuses on keeping DevOps in sync across teams in large organizations.Git as source of truth
  - A tool used for that is ArgoCD.
    - ArgoCD is a CRD so running in K8s.
    - Entire setup for argo CD as manifests.
    - ArgoCD watches for changes and sunsets them if necessary.Something like protecting dev/main branches in github/gitlab.
    - Argo Project consists of argocd, argo workflows, argo rollouts, argo events.
      - Named after mythological ship Argonauts - Logo of argo is an orange squid.
