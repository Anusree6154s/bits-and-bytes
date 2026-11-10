---
layout: default
title: Graphql vs Rest API
permalink: graphql-vs-rest
date: Nov 11, 2026
excerpt: Understanding diff b/w Graphql and Rest API
parent: API Architecture
---

# GraphQL vs Rest api

- Rest is the default choice for most applications.
- GraphQL is useful for frontend flexibility.
  - Frontend flexibility includes:
    - multiple frontends - Web, mobile, admin portal, partner portal.
    - FE very frequently need diff combinations of existing data. user configurable dashboards & reports. deeply connected data models. eg - Github, Shopify, Netflix, Facebook, Reddit.

* Most GraphQL features are available in BFF (BE for FE) architecture. So GraphQL is mostly useless.

# SSE vs Websocket (Rest api still always better than these open connections)

- SSE - Server sent events.

- way for server to continuously push updates to a client via HTTP. one-way
- switch (notification, live dashboard, logs, tokens) Web socket - continuous message from both client and server. both use an open connection (not polling). SSE uses HTTP connection. websocket starts as HTTP and then upgraded to websocket protocol where messages are exchanged as websocket frames.
  (chat apps, game, collab editing) DNS and TLS/SSLDNS - assigns registering a static IP of a website and buying a domain name. TLS - transport layer security.
- encrypts data sent b/w client & server.
- modern version of ssl (secure sockets layer)
- HTTP + TLS = HTTPS. Page 25Express vs Fastify vs NestJS - Express - slow + unstructured.
- Fastify - fast + unstructured.
- NestJS - slow + structured.
- NestJS + Fastify - moderately slow + structured, using fastify. For large projects w/ nestjs, using fastify along w/ it does no much performance improvement. Istio-ingress- An alternative to nginx ingress.
- Ingress fundamentals: K8s ingress (needs an ingress controller like nginx, traefik, HAProxy, etc.). Focused on layer 7 (HTTP) routing.
- Nginx is said to be basic layer 7 routing.
  Istio is a advanced layer 7 routing b/c it provides much more than nginx through at layer 7, like traffic splitting, canary deployments, retry policies, circuit breakers, mTLS, observability, fault injection.
- Layers (Comp. Sci network model term) 3 Network models :- OSI Model, TCP/IP Model, Hybrid TCP/IP model. OSI model - created by ISO.  
  Page 26(32) - OSI (Open Systems Interconnection)
  ISO (Internal Organisation for Standardisation)
- 7 layers conceptual model. Not used in real world. Used by k8s for theory purpose.
- 7 model:- layer 7 - application layer 6 - presentation layer 5 - session layer 4 - transport layer 3 - network layer 2 - data link layer 1 - physical.
- layer details:- Application - user facing (- HTTP, HTTPS, HTTP, HTTPS, DNS etc Presentation - data format, encryption encoding TLS/SSL, PNG/JPEG,
  UTF8, ASCII Session - connection, session management SMB Session, TLS session)
  Net BIOS Page 27transport - End to end communication
- TCP, UDP, QUIC, network - routing - IP (v4/v6), ICMP, Data link - communication on same n/w
- ethernet, wifi, VLAN, MAC address Physical - Actual signal transmission
- copper cables, fibre optic, etc. TCP/IP model:-
- only 4 layers. used in reality
- layers include:- Application, transport, internet & n/w access
- hybrid:- how 5 layers application, transport, network, data link, physical other vendor specific layer models that are not commonly used by anyone:
- Istio-ingress
- Istio - service mesh platform.
- Contains controlplane (istiod), side car proxies (envoy), traffic management, mTLS, authorization policies, observability. ingress gateway - egres gateway
  all w/o touching the app.
- uses istio-ingress gateway which was envoy.
  (33) Page 28(34) - envoy, is a proxy that forwards requests, load balancer, TLS termination, metrics, collection, traffic splitting, etc.
- Other ingress fundamentals north south traffic - traffic to and from outside the app east west traffic - traffic within services of the app internals edge proxy - Proxy located at boundary of cluster
- Does TLS termination, routing, filtering
- istio ingress gateway is edge proxy load balancer - distributes requests across ingress gateway pods.
- provides stable public IP or DNS name cloud providers create it automatically Request flow:- user send req to public domain send - DNS resolve domain to public domain load balancer forward req to ingress gateway Gateway evaluate gateway resource Virtual service determine routing rules Request reach service and pods
- Istio-ingress gateway architecture
- Istio-ingress gateway deployment
- K8s deployment has pods, and these pods
- This deployment has pods, and these pods Page 29contain containers called as "envoy container".
- Purpose of istio-ingress gateway is to process incoming traffic.
- deployed within "istio-system namespace.
- can be scaled independently from main app.
- Envoy Proxy Name of high performance proxy used by istio can be used anywhere as a proxy.
  that's part of a software called "envoy" developed by "lyft" company. can be used anywhere as a proxy within istio - as sidecar proxy,
  as a container proxy within pods, etc.
- Gateway pods - pods running envoy.
- recieve requests from load balancer, apply gateway &, virtual service rules.
- can be horizontally scaled.
- Gateway selectors - selectors specific to istio
- enables multiple gateways
  in one cluster.
- Can support multiple ingress gateways, pee app.
- Also supports one dedicated gateway pee app.
  (35)  
  Page 30(36)GatewayED - for deploying istioother gateway resources :-hosts on istio (allowed domains) - server (listener definition) open protocols (HTTP, HTTPS, TCP, etc.)wildcard host - to match multiple domains like \*.example.com, multiple hosts listeners.Gateway binding (associating Virtual Services w/ gateways), Gateway lifecycle.Gateway binding references Gatewayvirtual services references Gatewayw/o binding routes don't apply.- Gatewayend of it cause this is rest - X -Istio vs nginx- istio provides what nginx provides plus service mesh (secure to service communication), mTLS (mutual TLS protecting traffic from service to service), traffic splitting as we want, observability, w/o modifying app code. Page 31(37)load balancingRound robin - load distributed sequentially & evenly across available servers. Weighted load balancing -Eg: upstream backend {server app1 : 3000;server app2 : 3000;}weighted load balancing - you weight servers. % wise upstream backend {server app1 : 3000 weight = 3;server app2 : 300 weight = 1;}- app 1 get 75% more traffic.least connections - traffic to least busy instance.upstream backend {least_conn;server app1 : 3000;server app2 : 3000;}Health check/failover - if app dies, traffic moves to app2.upstream backend {server app1 : 3000 max_fails = 3 fail_timeout = 30sserver app2 : 3000;}Page 32(38)sticky session load balancingupstream backend {ip_hashserver ...}upstream backend {sticky cookie srv_id expires = 1d;server apps ...}- can be based on IP or cookies etc.- not a load balancing algo, but rather a constraint that modifies load balancing behaviour.Realtime sys Vs Rest api- always rest api better of little latency & is valuable in comparison to open connections like web socket or SSE.- real time sys don't cook on serverless platforms, edge servers, etc.top Server sent to me (LOD)free -h - show availbee @ server-ip -p 2203 -free -h ouplays ram and swap, free & occupied.Page 33 (39)# LxC (Linux containers)- factsOS-level virtualisation - Not hardware virtualisation.Runs in containers on a host linux kernel.Acts like a small linux m/c.system container (like how docker is application container)Every container has its own - PID namespace, n/w namespace, mount namespace, hostname, filesystem, users (optionally mapped).Containers are isolated using linux namespace and cgroups.linux cgroups enforces following limits on lxc container: RAM, CPU cores, CPU time, disk quota, w/o bandwidth, I/O limits.Has singe host ckernles the kernel. Cannot boot a diff kernel inside lxc like windows on FreeBSD.host ubuntu kernellxc 1 (ubuntu)lxc 2 (debian)
  Performance (Compared to VMs):Faster startup, lower RAM overhead, better density (more containers per host).Persistence:Stays stuff installed on exe container remains installed even after reboot (less compared to VMs, bcz host kernel is shared).Security:Less vulnerability can affect all containers.Limitation:Linux guests only, cannot use different kernel version, some kernel features/modules depend on host; certain workloads (eg: some K8s or nested containers scenarios) may require extra configuration as workloads in VMs in K8s.# Advanced K8sStay basedDevops -> K8s -> K8s FundamentalsApplication packaginghelmchartsvalues.yamlchart.yamlhelm repositoriesGitops:Argo CDApplicationsApplication setsSyncReconciliationDrift detectionGit as source of truthContinuous delivery (CD)Progressive DeliveryRollbacksAutomated deploymentsPage 2 (Image 2)Without helmSuppose you have multiple services like frontend, backend, postgres, redis, ingress, etc. For each one will have to write deployment.yaml, service.yaml, ingress.yaml, configmap.yaml, secret.yaml, pvc.yaml, etc.This results in 20, 30, 50 yamls...For deploying in different environments like dev & prod we will have to copy that files multiple times.Too much work, duplicate files.With helmReduced duplication via templatesThus, it is most useful when used in combination w/ template expressions likePage 3 (Image 3)$values.xyz.yz But one can run "helm install myapp" without template expressions just with static data though it is same.(Running above mentioned command is called as installing a helm chart or installing a release.)Template files (with template expressions) are called value filesValue filesTo deploy different kinds of values to different environments (Eg: values-dev.yaml)Avoid duplicated manifests while still maintaining operationBinding to k8s env file, but w/o security.Charts.yamlAddition of it to any folder makes that folder a valid "chart" & makes helm recognise it as one installable package.Running "helm install myrelease my-app" (Installing a helm chart / release)In general, we don't push charts (folder created w/ charts.yaml) into OCI registries (open w/ charts.yaml) into OCI registries (open w/ charts.yaml). It is just spun on the repos required nodes.But in general, we push to OCI registries same as docker images (Eg: dockerhub, github container registry, Amazon ECR, Google artifact registry, Azure container registry).Page 4 (Image 4)Multiple charts by having multiple folders ref chart.yaml to install.Find patty charts to install, popular reusable packages/charts like prometheus, grafana, etc. redis, postgres, etc.Deploying / Installing multiple helm chartsHelm file used for describing multiple helm releases in one place, or deploying them together & volatile controlling, ordering & shared configuration.Gitops / ArgoCDSubset of DevOps.Focuses on keeping DevOps in sync across teams in large organizations.Git as source of truthA tool used for that is ArgoCD.ArgoCD is a CRD so running in K8s.Tantive setup for argo CD as manifests.ArgoCD watches for changes and sunsets them if necessary.Something like protecting dev/main branches in github/gitlab.Page 5 (Image 5)- Argo Project consists of argocd, argo workflows, argo rollouts, argo events.Named after mythological ship Argonauts - Logo of argo is an orange squid?
