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

[Continued in [here](#k8s-structure-and-visualization)]

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
| Process: node         |
|-----------------------|
| Linux Kernel Reserved |
|-----------------------|
```

- Each process getsisolated memory
- Kernel prevent process A from reading process B's memory

## Media Forge

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

## K8s Basics

So we are back to continuing with k8s basics dropping media forge in between 🥲🙂

### Linux Basics

<p align='center'><img src='https://github.com/user-attachments/assets/846c2d65-c0ac-4b9c-a929-6bf847ad297f' width=100/></p>

Back to understanding linux basics for k8s. They include processes, ports, networking, DNS, file systems, permissions, env variables, systemd, services, logs

- **Processes**:
  - A combination of program instructions, memory used, CPU execution state, open files, network connections, security identity, env variables is called a process
  - Process handling in physical rack server
    - CPU core execute process instruction
    - RAM store process data
    - Disk (HDD/SSD) store process file
    - NIC/network card process network traffic (send and receives network packets)
    - Linux kernel schedue CPU time between processes
  - Physical rack visualization

    ```
    |-------------------------|
    | CPU                     |
    | RAM                     |
    | SSD/HDD                 |
    | NIC                     |
    | |----------------|      |
    | | Linux Kernel   |      |
    | |----------------|      |
    |-------------------------|
    ```

    - NIC
      - Network interface card
      - Hardware for network communication like via ethernet ports, fibre ports, wireless radio hardwood
    - VIsualization

    ```
    Nestjs app -----|
        |           |-----Application
        v           |
    Socket API -----|
        |
        v
    Linux Kernel Networking Stack
        |
        v
    NIC driver -----------------|
        |                       |
        v                       |
    NIC hardware                |------- Hardware to communicate via sockets
        |                       |
        v                       |
    Ethernet cable/ network ----|
    ```

- **Ports**:
  - Communication endpoint
  - Use ports to decide which process receives incoming n/w traffic
  - Kernel does forwarding of n/w from ports to its associated process
- **Networking**
  - Just basic concepts of who connects by what
  - Eg: Ethernet cables/fiber connects server, cables connect to switches, etc
- **DNS** (Domain Name System)
  - Converts domain names to IP address, via which servers communicate
- **File systems**
  - organize data on storage systems
  - eg: SSD, HDD, etc
- **Permissions**
  - Eg: -rwxr-x---
  - Rules followed in permissions:
    ```
    `- rwx r-x r--`
     | |-| |-| |-|
     |  |   |   |
     |  |   |   v
     |  |   |   other permission
     |  |   v
     |  |   group permission
     |  v
     |  owner permission
     v
     Filetype
    ```
  - filetype
    - `-`: regular file
    - `d`: directory
    - `l`: symbolic link
  - permissions - `r` read, `w` write, `x` execute, `-` no permission
  - Numeric representation
    - `r` - 4
    - `w` - 2
    - `x` - 1
    - `rwx` - 7
    - `r-x` - 5
    - `---` - 0
    - `- rwx r-x r--` - 750
    - Can be used as `"chmod 750 filename"`
- **Env variable** - As we know it
- **systemd / services**
  - `systemd`
    - linux service manager
    - controls starting, stopping, restarting services, etc.
    - `eg services` -> nginx, ssh, docker, etc.
    - `command` -> `"systemctl status"`
- **Logs** - As we know it

### Containers

<p align='center'><img src='https://github.com/user-attachments/assets/40e5e9aa-bdae-4c09-9996-a22745908366' width=100/></p>

Images, containers, layers, volumes, networks, entrypoints, env variables, multi stage builds.

- **Images**
  - packaged filesystem
  - metadata used to create container
  - contains application files, libraries, runtime binaries, default config, startup command.
  - readonly templates
  - when container starts
    - mount image filesystem
    - add a writable layer
      - copy files from readonly to writable files & run from there
    - start process
- **Container Runtime**
  - eg: docker, containerd
  - creates containers (processes from image), configure namespaces/cgroup, mount filesystem, set networking, start process
- **Container**
  - Process made from image
  - Eg: running "docker run redis"..
    - creates redis process
    - creates isolated filesystem
    - creates virtual n/w interface
    - creates writable container layer
- **Layers**
  - something with which images are built.
  - each Dockerfile instruction creates a build tor file/file/folder, that is a new filesystem layer.
  - Each tor file/folder created is immutable, and each of them is called a layer.
  - Container stacks them using OverlayFS (a linux filesystem tech that allows multiple directories/filesystems to be stacked together into one unified filesystem view).
- **Volumes**
  - Persistent storage for containers outside container lifecycle.
- **Networks**
  - Docker creates virtual networking using:
    - linux bridges
    - Virtual Ethernet interfaces (Veth)
    - NAT rules
    - routing tables
  - _Linux bridge:_
    - virtual software switch to which containers connect to; called "docker0"
    - created by docker.
    - Visualisation

    ```
    `container A` ---\
    `container B` ----> `"docker0" bridge --> `Host NIC` --> `Internet`
    `container C` ---/
    ```

    - Part of virtual network interfaces

  - _Virtual Ethernet interfaces (Veth pair)_
    - created by docker during container start
    - called as "virtual cable pair" (veth pair)
    - part of virtual network interfaces.
    - has one side inside container (`eth0`), one side outside container (`veth7abc123`)
    - visualisation:
    ```
    container eth0 <--- virtual cable ---> host veth xyz
    ```
  - _NAT rules (Network Address Translation)_
    - Networking Address Translation rules
    - Rules/Instructions to how packets (that travel through sys) must be rewritten.
    - This rewriting allows containers w/ private IPs to access host's internet via host IP (translation).
    - Rules exist because not every packet must be translated.
    - Eg commands: SNAT, DNAT, MASQUERADE, REDIRECT.
    - This is not just of docker but of host system, linux in general, VPN, etc too. (used everywhere for rewriting packet addresses)
    - It is a subset rule among many other rules in linux iptables.
      - _ip-table_
        - tool/sys/networking/firewall utility.
        - iptable defines what happens to packets.
        - used for managing packet rules.
        - eg:

        ```
        iptables
        |--- filter rules
        |--- forwarding rules
        |--- logging rules
        |--- NAT rules
        ```

        - eg of iptable rules:
          - Allow incoming SSH traffic
          - Rewrite packet source IP.
          - . . . etc
        - Answers questions like allow packet?, block packet?, rewrite IP?, forward IP?, log packet?

  - _Routing Tables_
    - Answers questions like where to hop next, which network interface should transmit the packet, etc.
    - decides where the packets go to.
    - In terms of docker, this decides which packets go to that container related packets go to docker0 (linux bridge), while internet traffic go to router etc.

- **Entry Points**
  - main command started when container launches.
  - Eg: ENTRYPOINT ["node", "server.js"]
  - When the process marked as entrypoint (here it is "node server.js"), it becomes PID 1 process.
- **Env Variables** (same we know it)
- **Multi stage builds**
  - We can have multiple stages in dockerfile by writing like this - "FROM xyz as abc".
  - Generally all commands in dockerfile creator makes one layer.
  - All layers all together makes one stage.
  - And this stage builds itself to create one image which is referenced by docker to run in the container.
  - With multistage builds, only the final stage is referenced as the image created by the dockerfile
  - During each stage in multistage builds, multiple stages (few stage images / temporary stages) are created (collection of layer files) and stored in disk. But only final stage image is exposed to docker & becomes the o/p.
  - Benefit : smaller containers, faster deployments, reduced attack surface, lower memory/storage usage.

### Purpose of K8s

<p align='center'><img src='https://github.com/user-attachments/assets/aaa7d857-4270-44f8-a848-9b834f0c1b53' width=100 /></p>

#### Problem and their solutions via k8s

- Container crashes —> self healing
  - w/o containers K8s, need to manually up stuff
  - K8s continuously watches containers
  - w/ containers K8s, RAM etc re-allocation, filesystem remounting, network interface recreation etc is taken care of.
- multiple server -> scheduling
  - K8s simplifies scheduling pods into free servers w/o having to manually track it via scheduler
- Traffic routing -> services
  - K8s services allow having stable traffic routing to healthy BE pods w/o manually having to handle it.
- Scaling -> Replica Set via Services
  - Distribution of load across back servers automatically done by K8s w/o manual intervention under higher load via ReplicaSet
- Config management -> configmaps / Secrets
  - Diff env config & secrets injected into container memory w/o rebuilding using K8s.
- Deployments -> Rolling updates
  - Updates applications w/o downtime via K8s.
  - Process: — start new pod, wait until healthy, stop old pod, repeat gradually.
- Service discovery -> DNS
  - K8s provides internal DNS to communicate set of pods even when they move frequently b/w back servers.
  - Process: — Application attempts to DNS lookup, req sent through DNS Virtual n/w, cluster DNS responds, app server receives current service IP.
- Resource Control -> Requests / limits
  - To avoid applns from competing for hardware resources, we can set request limits & limits for cpu, memory, etc in k8s deployment manifest (or any other manifest that has deployment spec). This set hardware resource limits on containers (not on pod or node).
- Receiving K8s Architecture First
  - Cluster
    - group of physical/virtual servers working together to run applications
    - Consists of control plne and worker nodes
  - Control plane
    - management brain of K8s.
    - doesn't normally run an appln container
    - Responsibilities :- accept requests, store cluster state, make decisions, monitor cluster status, command worker nodes.
  - API server
    - front door of K8s (and through it)
    - Everything talks to it :- kubectl, scheduler, controller manager, kubelet - Responsibilities — validate req, authenticate user, authorize action, store resource obj.
  - etcd
    - K8s db. Stores cluster state
    - Also writes to physical storage devices (CRI, CSI, etc)
  - scheduler
    - decides which node the pod must go to.
    - a process running on control plane
  - Controller manager
    - continuously check desired state vs actual state
    - a process on control plane that keeps doing - observe, compare, correct (called as reconciliation loop).
    - reason why K8s correct itself
  - kubelet
    - agent running on every worker node.
    - receives instruction from control plane
    - ensures containers are running
  - Container runtime
    - runtime that actually runs containers
    - eg: containerd, CRI-O
    - Process :- Pull required image, create filesystem, configure networking, start process
  - kube proxy
    - manage n/w rules for services.
    - when traffic arrives at a service, kube proxy routes it to correct pod based on iptables / networking rules.

#### Most important K8s concept (Desired state reconciliation)

- Desired state reconciliation
  - We declare desired state (eg: replicas 3) and K8s try to match it to reality via reconciliation loops
- Self healing
  - basically reconciliation fixing failures
  - cluster repairing itself
- Auto recreation
  - K8s automatically recreates missing resources
  - Eg: Someone manually deletes a pod. But desired state says it needs 3 replicas, & reality has only 2 pods, so controller immediately creates another pod.
- Controllers
  - software that perform reconciliation
  - Reconciliation loop :- controller continuously watching, comparing, acting & repeating
  - A linux process running on control plane service
- Deployments
  - stores desired appln state  
    (deployment is the instruction, controllers perform the instruction)
- Scaling
  - changing desired capacity
  - eg: from replica: 3 to replica: 10
- Rollback
  - change desired state to prev version

#### Learn Objects

- Phase 1 - Pods
  - what:
    - smallest deployable unit in K8s.
    - The thing that k8s schedules into worker nodes
    - contains >= 1 containers
    - not a process itself.
    - a K8s object that run & manages the process (aka :- container)
    - pod & container :-
      - pod = wrapper
      - container = isolated process env

      ```
      pod

      container A         container B
      |-------------|     |-------------|
      | process A   |     | process B   |
      |-------------|     |-------------|
      ```

      - a pod provides shared n/w, shared storage, shared lifecycle.
      - multi containers Pods - pods can have multiple containers
      - pod lifecycle Green
        - Pending -> Pod created, image downloading, waiting for node.
        - running -> containers started, app "running"
        - Failed -> container crashed - pod failed
      - logs — "kubectl logs my-pod"
      - Exec into pod :
        - "kubectl exec -it my-pod -- sh"
        - allows to start a command inside a running container.

- Phase 2 — Deployment
  - Replica set - ensure specific no. of pods exist
  - Scaling - Change no. of pod replicas
  - Rolling updates - update application version gradually
  - Rollback - revert back version
- Phase 3 — Service
  - Service - Provides a reliable n/w endpoint for pods
  - Cluster IP :
    - IP for internal cluster communication.
    - So that traffic remains inside cluster networking & no external traffic reaches it.
  - Nodeport
    — port used to expose a service through a worker node's IP.  
    — can be accessed from outside cluster cluster IP  
    — common uses includes connecting external load balancers, for development & testing quickly.
    - expose app "1010 DNS or load balancers, etc.
    - Eg for NodePort & Node IP. "http://Node-IP:30050"
    - worker node listens to this TCP port.
  - Load balancer
    - for exposing services externally. & forward traffic to cluster nodes
  - Service discovery
    - Service discovery is done via service names
    - It is done so that pods can move around w/o breaking communication
    - A service can point to multiple pods like redis-service can have multiple replicas of pods, but all can be accessed by same name.
  - kube-dns/coredns
    — DNS server K8S
    - just another pod running on worker node CPU's & RAM
  - Label selectors
    — labels used for services to find pods
    - Eg:
    ```
    Pod
      "label:
          app: backend"
    Service
      "selector:
          app: backend"
    ```
    Now K8S matches them.
    - labels are metadata stored in it.cd
- Phase 4 — Configmap & Secrets
  - Env variable injection
    - Eg: Config map contain env variables, containers can access them inside process env.[var-name]
  - Mounted files
    - Provide config as files instead of env variables
    - Eg: Config map has app.conf. It is mounted in containers as /etc/config/app.conf
    - to app "it looks like normal file on disk"
    - (means file contents become visible inside filesystem namespace, just like a normal file).
  - Separation of config from image  
    — container image is kept independent from configuration  
    — ie, when config changes per namespace like diff for prod & dev, the image of container is unaffected.
  - Secrets
    - store sensitive config
    - consumed as env variables or mounted files.
- Phase 5 — Ingress
  - Reverse proxy
    — receive req & forward it to execution
    - Ingress controller: is a process running on worker node CPUs.
    - Eg: user requests at [https://example.com](https://example.com) ingress receives it & forwards it to frontend-service.
  - Routing
    — a thing that reverse proxy does.
    - deciding which service gets the incoming req.
  - Domain name
    — human readable names created from Service names instead of IP addresses.
    - DNS resolves the domain to the ingress endpoint
    - Traffic then flows through switches, routers, NICs, and into the cluster
  - TLS termination — handle HTTPS encryption  
    — TLS = Transport layer security.  
    — Ingress terminates TLS (stops encrypted traffic & decrypts it by security)
    - it decrypts & forwards the req internally.
  - NGINX ingress controller
    - perform the ingress functionality based on ingress obj stored in etcd.
- Phase 6 — Storage
  - Volumes
    — provide storage to pods  
    — Volume ultimately resides on SSD, NVMe (solid state device), NVMe, & HDD, n/w storage
  - Persistent Volume (PV)
    — declares/represents actual storage available to the cluster.
  - Persistent Volume Claim (PVC)
    - Storage requested by pods
    - Eg: Pod requests "I need 50GB". K8S find a matching PV & binds Pod & PV. Pod don't care which disk provides the storage.
  - Stateful Workloads
    - Apps / Pods which are not stateless
    - Eg: PostgreSQL, MySQL, MongoDB, redis
    - When these pods restart, the process change from old to new container, but same volume/storage is used.
- Phase 6 — Networking Fundamentals
  - Pod net networking
    - Every pod gets its own IP & each one communicates to other via these IPs.
    - Packets of data need to travel through these to reach from one pod to another via network :-  
      Pod 1 - VETH (virtual n/w interface) - worker node NIC - switch - other worker node - destination pod.
  - Service virtual IPs
    - Eg: "backend-service"
    - stable addresses for a group of pods.
  - kube-proxy
    — routing btw pods internally based on service names.
    - it also configures networking rules on every worker node.
  - CNI plugin
    - Container Networking Interface
    - Create Pod networking.

## K8s Structure and Visualization

So we're back to understanding K8s now that we've taken a round of understanding the undelining linux basics.

### Visualisation

A data center looks like this

```
Datacenter
|--- Rack
|    |--- Server 1
|    |--- Server 2
|    |--- Server 3
|--- Rack
     |--- Server 4
     |--- Server 5
     |--- Server 6
```

- Different servers on diff racks can be part of same Kubernetes cluster.
- When multiple servers have cost check, certain requirements, they are as associated of k8s, they are then part of k8s cluster. -

### K8s terms

- kubelet
  - small local agent/process
  - Exists on every worker node / control plane node.
  - Make sure containers/pods runs correctly on that m/c.
- Tasks of kubelet :
  - talk to api server, receive pod assignments, start/stop containers, report node health, report pod status, mounts volume, handle probes.
- kubectl
  - Pronounced "kyoobe-cuttle" or "kyoobe-control".
  - Exists on developer laptop / admin m/c / control server.
  - It communicates of kube-apiserver.
- kube-proxy
  - Kubernetes n/w proxy.
  - exists on every worker node (as daemon/fbg process).
  - It handles k8s n/wing rules inside cluster Eg: Service virtual IPs, load balancing, traffic forwarding, ip tables / ipvs rules.
- kubeadm
  - K8s admin / bootstrap tool
  - exists on control plane m/c.
  - worker setup m/c
  - used during cluster creation for creating control plane "kubeadm init" & join worker pods "kubeadm join", etc...
  - Not part of ras running cluster logic instead part of cluster installation / setup tool.
- kube-apiserver
  - main entry point for k8s cluster. Everything talks to this. Acts like central management api. - Exists on control plane server.
  - Talks to kubectl, kubelet, scheduler, controller-manager, etcd.
- kube-scheduler
  - chooses which node runs pods. (decision engine)
  - Exists on control plane server. Chooses where worker node try maintains desired state pods.
  - talks to kube-apiserver, worker nodes indirectly.
- kube-controller-manager
  - Exists on control plane server.
  - Maintains desired state.
  - Talks to :- kube-apiserver, etcd ... indirectly.
  - Runs reconciliation loops (loops inside k8s that continuously check desired state vs actual state).
  - eg: desired replica = 3, actual replica = 2. Then create another pod.
- etcd (etc distributed) (et-see-di)
  - etcd directory / distributed key value db (like redis)
  - store cluster state db.
  - most critical k8s db (source of truth).
  - Exists on control plane servers.
  - Stores :- pods, deployments, services, [as key-value pairs] nodes, secrets, cluster desired state.
  - _distributed_
    - it is called distributed bcoz multiple etcd servers can work together.
    - eg if multiple control planes with diff etcd, they communicate via a "Raft consensus" algorithm which stores a copy of the cluster state, thus preserving data even if one etcd beads down. (cluster state is not the same as control plane).
- containerd
  - container runtime (actually runs containers)
  - Exists on worker node.
  - Talks to kubelet through CRI.
- CoreDNS (Core Domain Name Sys)
  - K8s - Internal cluster dns.
  - lets pods communicate using names. eg: api-service.default.svc.cluster.local. - usually runs as pods on worker nodes.
- Container Network Interface (CNI)
  - Provide pod networking.
  - Exists as CNI plugins on worker nodes.
  - eg: Calico, Flannel, Cilium.
- CRI
  - Container runtime interface.
  - Standard interface btw. kubelet (node agent) & container runtime (containerd).
  - Types of communication being done via here include kubelet asking to pull image, start container, stop container, delete container, get container status, etc..
- CSI
  - Container storage interface.
  - Standard way k8s interact w/ storage systems.
  - Exists on worker node, control plane (occasionally on worker node, control plane)
- Pod
  - Small deployable unit holding one or more containers together
  - Runs on worker nodes inside container runtime (containerd)
  - Contains 1 or more containers, shared n/w, shared storage, shared localhost
  - e.g., k8s Pod
  - e.g., pod may contain:
    - nodejs API container
    - sidecar logging container, etc.
- Deployment
  - An object that is stored in etcd (API resource)
  - It is used to keep a permanent record of the desired state of cluster
    - Deployment controller continuously checks actual state against the desired state stored in deployment object (key-value pair) stored in etcd
  - It is generated by k8s from the deployment.yml file (also called deployment manifest) upon running a command like "kubectl apply -f .yaml"
    - It can also be generated from a json file or directly from terminal like "kubectl create deployment --image=". In such case kubectl itself creates a deployment object based w/ configuration based on kubectl defaults, k8s, defaults by API server generated metadata.
  - Also handles replicas, rolling updates, self healing, rollout history
- Replica set
  - replica = copy, set = collection
  - it is an API resource (cluster resource) whose instance is stored within etcd
  - Deployment controller, from developer / cr server sense kube controller manages, creates a replica set.
  - Though replicaset obj can be created from a riperi [replica] <missing text: "set"> manifest like deployment
  - it is generally auto-generated by deployment controller. The trigger for creating a replicaset is the appearance or change of deployment object. If expected no. of replicasets are 3 & these objects are 3 & deployment controller creates the extra one.
  - it manages the no. of pods to be kept up
- Service
  - Objects that defines a service name that also becomes the DNS name inside the cluster (we can also set a static IP for that service that falls in its cluster's service IP range & must be unique). It is this DNS name kube proxy will use to get incoming calls to BE from FE & then re-route to actual IPs of each pod that gets generated
  - created by user themselves via kubectl (like deployment obj) using a source manifest & stored in etcd
  - Endpoint Slice Controller, watches service objects & Pods, it also creates endpoint slice objects for the service.
    > The objects stored in etcd can be multiple in number (eg: multiple service, deployment, replicaset objects, etc.). They can be multiple depending on diff manifests or based on diff namespaces  
    > eg: → etcd A
        |  ↳ deployments
        |  ↳ dev
        |  ↳ staging
        |  ↳ prod
        |  ↳ services
        |  ↳ dev
        |  ↳ staging
        |  ↳ prod
        |  ↳ pod
        |  ↳ dev
        |  ↳ staging
        |  ↳ prod
        → etcd B (same thing)

> All the etcd's of the same cluster will shared this segregation based on namespaces & such.
> (so that if one etcd goes down, others still have data)

- Ingress
  - meaning → incoming traffic
  - it routes external HTTP / HTTPS traffic into cluster.
  - created from ingress manifest by the user/developer using kubectl .
  - It is an api cluster resource stored in etcd, it is called ingress object
  - Ingress controller watches the ingress objects. It is deployed along with other pods as one among them like:

  ```
  Node A → App pod
         ↳ App pod
         ↳ nginx ingress controller pod
  Node B → App pod
         ↳ App pod
  ```

  - Based on ingress object config, ingress controller manages the routing. -

- namespaces:
  - means a boundary that keeps names from colliding
  - it is used for policy checks
    - Eg:
      - Resource Quota: Pod belongs to prod --> check prod quota
      - RBAC :- user accesses prod namespace --> check permissions
  - When we provide namespace to any manifest file, it creates multiple objects from that manifest file for each namespace.
- stateful set
  - Most k8s workloads / pods are managed by a "Deployment" • But when a pod dies and when "Deployment" recreates the pod, the new pod recreates the pod, the IP & node can have suff name, IP & node. This is called stateless • This is generally used for- FE, API, servers, etc.
  - But some applications care about identity of the pods created & are not interchangable. In such case use "Stateful set"
  - Deployment pods look like api-6f84... etc, & every recreated pod gets a new name. stateful set pods look like postgres-1, postgres-2, etc out fixed names. each pod also gets a predictable pod name. This is very important for databases, distributed systems, cluster membership.
  - this works in association of persistent volume claim (PVC). Each pod gets its own storage which wont get destroyed when the pod gets destroyed. when a pod is recreated it attaches the same PVC as the older pod.
  - Ordered startup
    - In Deployment, "create 10 pods", k8s may start them in parallel.
    - But stateful set starts in order: postgres-1 → postgres-2 → postgres-3, etc Similarly during shutdown, it stop db's in reverse order.
    - this is because many distributed dbs require db 1 to start bt db2, b2 db 3, etc.
  - ordered updates
    - Pod deployment generally updates pods in batches. But Stateful set updates pods one after another. this is ordered rollout and generally useful for dbs.
  - stateful set components
    - when we apply "kind: StatefulSet" ; k8s creates a statefulset object stored in etcd. statefulset controller watches it. Statefulset controller then creates pods like postgres-1, postgres-2, etc based on the desired no. of pods mentioned in stateful set object being watched.
- Daemonset
  - A k8s resource that ensures one copy of a pod runs on every matching node.
  - called daemonset because it is a set of
    - daemon-like pods running on nodes daemon → a background process that run continuously in background.
    - Example: we want to run a log collector on every node

    ```
    Node A → log collector
    Node B → log collector
    Node C → log collector
    ```

    - Deployment can't guarantee this, it creates N replicas somewhere. (sometimes on one node)
    - But daemonset guarantees 1 pod per node.
    - Working:
      - We apply "kind: Daemonset"
      - kubectl reads the yaml file
      - API server authenticate
      - Daemonset object gets stored in etcd
      - Daemon controller watches daemon
      - By default it creates 1 pod per matching node.

      > We cannot tell daemonset how many pods to sunper node. We can only say to run current pod in every node.
      - Eg of usage for :- kubeproxy, log controller, monitoring agents.

- Job:
  - A k8s resource that tails, does same work
  - used for stuff like pdf generation, db migration
  - When deployment fails there is no further management as to retry or anything else. But when we configure job we can either retry or mark job as failed.
  - Can run parallel jobs
  - Flow:
    - Job obj stored in etcd
    - API server exposes it
    - Job controller watches Job obj
    - Job controller creates pod objects
    - Pod succeeds or fails Pod runs tasks
    - Job task succeeds go fails.
    - Job controller creates new pod if retry enabled, else marks Job as complete
    - Pod remain
- CronJob:
  - K8s resource that creates job on schedule.
  - Create from CronJob manifest by kubectl & stored in etcd
  - CronJob controller watches CronJob via API server. When it is time, CronJob controller creates a Job obj.
  - Job controller creates job obj & creates a pod, Pod runs.
  - Pod succeed succeeds or fails. Retries if configured.
  - Job complete : Pods still remain
- Secrets:
  - a K8s resource stored in etcd via terminal command for sake of safety. (bcz yaml file will record the secrets which we do not want)
  - We then reference the secrets obj name in deployment manifest, which will fetch the secrets directly from secrets obj. (eg: password)
- Config map:
  - To store stuff like hostname, ports numbers, feature flags etc. (Non-sensitive data)
  - A K8s resource stored in etcd from manifest
- Volume
  - Data storage
  - Specified as part of deployment manifest.
  - The actual data maybe stored within node/VM's real disk or cloud or NFS (Network File system), but to the container it will look like it is coming from a folder within the container files.
  - Specification example:
    ```yaml
    volumes:
      - name: data
      mountPath: /data
    ```
  - It is specified as part of pod template in deployment manifest. When deployment controller creates pods each pod gets a volume named 'data'. Just part of pod specification.
  - When pod is destroyed, the volume directly from container path will also be destroyed. When the directory gets destroyed, the associated actual db ins volume on disk also loses files in it.
  - Cons of volume per pod.
    - It is tied to pod life
    - Every pod will need to have volume specified
- PV (Persistent volume) (Static Provisioning)
  - cluster level K8s obj stored in etcd created from PV manifest
  - Actual storage is on Node disk/cloud/NFS.
  - This object is created only for creating a... [continues to next page]
  - volume within the cluster for a ahead change in the volume, we use PVC.
  - Flow of creating PV volume in list
    - Fuse you create volume yourself.
    - Then just reference it in pv object. (This method is not used anymore)
- PVC (Persistent Volume Claim):
  - Dynamic provisioning:
  - obj created from PVC manifest in etcd.
  - A storage controller notices PVC is pending & provisions storage.
  - eg: create EBS disk, GCP persistent disk, etc.
  - It then creates PV obj. & binds it to PVC (EBS, GCP disk, etc).
- Node: Physical/virtual server.
- Cluster: Group of physical datacenter servers.
- Kube-system:
  - Namespace object stored in etcd.
  - created automatically during bootstap of control plane. (Eg: kubeadm init)
  - Part of other predefined yaml manifests
  - of system components : CoreDNS, kube-proxy, networking plugins (cni), etc.
  - Created by Namespace controller. It also creates default, kube system, kube public
  - Kube-node-lease:
  - Purpose: holds K8s internal components.
- Sidecar:
  - Auxiliary container that runs inside same pod as main application & enhances or supports it.
  - has same network namespace (cannel, localhost shared), same storage volumes. (can be shared)
  - has separate process space (different container), separate lifecycle (can restart independently)
  - used to add functionality to or modifying main application code.
  - Eg:- logging, monitoring, proxying, security, configuration sync.
- Init Containers:
  - temporary container that runs before main application
  - used to prepare env required by app (eg: wait for db/cache readiness, download config or secrets at runtime (sun DB migrations))
  - Not commonly used for smaller apps, but sahay for prod k8s systems, microservices
  - w/ dependencies, etc.
  - created from Pod yaml manifests.
  - spec -> initContainers -> Turns into pod object.
  - If initcontainers are omitted, pods start directly with containers
  - Developer defines it, K8s creates pod obj, kubelet executes based on pod objs.
- Helm:
  - means ships steering wheel (k8s logo)
  - package manager for K8s. Bundles K8s yaml manifests into reusable, versioned packages called charts.
  - not a core component of cluster -> It is a cli tool on our m/c or CI/CD pipeline.
  - talks to K8s API server, applies manifests into cluster.
  - Without helm you need to manually manage multiple yaml files, repeated configs across envs, hard to version & reuse
  - Deployments:
    - with helm, everything is packaged, configurable via values, easy install/upgrade/rollback.
  - Helm Chart:
    - Chart
      - package K8s applicationist
      - contains templates values & chart yaml files
    - Template - K8s yaml templates
    - values.yaml - configurable params
    - chart.yaml - metadata (name, version)
  - Structure:

  ```
  my-chart/
  |--- chart.yaml
  |--- values.yaml
  |--- templates
        |--> deployment.yaml
        |--> service.yaml
        |--> configmap.yaml
  ```

  - Working of helm:
    - You install a chart: `helm install prometheus prometheus-community/prometheus`
    - Helm renders templates: - replaces placeholders in yaml.
      - Eg: `image: {{Values.image.repository}}` becomes `image: prom/prometheus`
    - Helm applies manifests:
      - helm sends final yaml to K8s API server
      - eg: deployment, service, configmap, ingress, etc.
    - K8s stores it in etcd like other normal resources.
  - Key features:
    - Allows install of packages called charts, like prometheus, grafana, nginx, ingress, postgresql.
    - Versioning/rollback supported: "helm rollback my-release 1"
    - Reusability: Same chart works across dev, staging, prod. Just change values.yaml.
    - Upgrade/update cluster resources safely: "helm upgrade my-app /chart"
  - Comparison of helm vs normal kubectl:
    - Without helm: use kubectl apply on every yaml file. No release history, nothing.
    - With helm: use helm install my-app name.
    - eg. internally it will pull templates yaml, values.yaml, generate less yaml. internally apply them (like kubectl), store release history.

- Operator:
  - K8s extension that automates full lifecycle of complex applications using CRD (Custom Resource Definitions) & Custom Controllers (reconciliation logic).
  - It acts like a system administrator ("operator")
  - In normal K8s, it can manage stateless apps (deployments), basic scaling (HPA), simple configs.
  - But it struggles with stateful, complex systems like Postgres databases, kafka cluster, elasticsearch, etc.
- A cluster is multiple pods spun within same K8s cluster related to same application for complex purpose. Like :-

```
k8s
|--> nestjs Pod (Our own app)
|--> postgres-primary-------|
|--> postgres-replica-1     |---> postgres cluster
|--> postgres-replica-2-----|
```

- CRD obj is stored in etcd
- It is watched by operator controller. specific to the cluster we want (Postgres, kafka) . The cluster specific operator is installed in K8s cluster, via operator manifest in which in the deployment section, the location from/image from where the operator needs to be installed is mentioned. This installed operator will take care of replicas, replication, failure, backups, upgrades, etc.

> Deployment section example in operator
> ```yaml
> kind: deployment
> containers:
> - image:
>   Some-company
>   postgres
>   Operator: v1
> ```

- CRD (Custom Resource Definition):
  - lets us add new resource type to K8s. (that are not built-in like kind:Pod, kind:Service, kind:Deployment, etc)
  - Examples for new resource types:
  - kind: kafkaCluster, kind: PostgresCluster
  - Added it is defined in operator manifest in CRD section, which only fully K8s that one specific type of obj exists.
  - The actual creation of object for that cluster is dependent on custom resource file (the manifest specific to that object)
  - eg. If CRD section in operator.yaml
  ```yaml
  kind: CustomResourceDefinition
  spec:
    names:
      kind: PostgresCluster
  ```

-> Custom Resource (CR) example# postgres-cluster.yamlkind: PostgresClustermetadata:name: my-dbspec:instances: 3API Group:-> so when K8s cluster is made storing it is installed. kubeapi server comes along w/ it. In kube api server, along w/ it comes some built-in API (sources) -> These APIs are exposed to outside K8s to which HTTP API calls are made by kubectl (http client)-> Built-in API groups are some groupings made by K8s for these api paths for each resource type.-> Built-in API groups & paths:CORE (no group)api/v1-> pods, services, configmaps, secrets, nodes, namespacesPage 12 (Image 12)app. (/apps/apps/v1)-> Deployments, Replicasets, Statefulsets, Daemonsetsbatch (/apis/batch/v1)-> Jobs, CronJobsnetworking (/apis/networking.k8s.io/v1)-> Ingress, NetworkPolicyautoscaling (/apis/ /HPA)These all are compiled into kube-apiserver.Additional APIs-> Generate via CRDS.-> kube-apiserver dynamically registers new route when user creates CRD.-> wee get new api path like apis/[mycompany.com/v1/resources](https://mycompany.com/v1/resources).-> Aggregated API server (Advanced). External API server can also plug into kube-api server.-> Most of the conversations with K8s cluster between kubectl, kubelet, etc, controller schedules with kube-api server.happens via http/https rest & watch api calls & requests & these api pathsPage 13 (Image 13)-> when writing manifest files, we mention the api path associated with its resource type so that kube-api server can do it like this :-apiVersion: apps/v1kind: DeploymentapiVersion: v1kind: PodapiVersion: batch/v1kind: Job ... etcThis is done so that when these manifests are applied, kube-api server can do the following:-Parse apiVersion + kindFind matching resource handlerValidate schemasRun admission controllersDefault missing fieldsStore object in etcdAdmission Controllers-> So when a request is made to K8s cluster via kubectl, a lot of stuff/checks happen w/ admission controllers.Page 14 (Image 14)just part of it.-> Stuff that happens after req from kubectl to kube-api server:-kubectl apply deployment.yaml (via http req)kube-api-server:http routing(matches apiVersion = apps/v1, kind = Deployment)authentication(verify who is making the req)authorization(verify if authenticated user is allowed to make req)request decoders(convert manifest to resource obj)API resource lookup(kube finds appropriate handlers from internal api-registry to handle [apps/v1, Deployment])Decoded resourceobj (chain of) (built-in)Admission chain (chain of)-> service account controllers(injects default secure account)-> default storage class(adds default storage class if omitted)Page 15 (Image 15)-> limit ranger (applies/enforces resource limits)-> Pod security (checks security requirement)-> resource quota (check namespace quota)-> Mutating Admission Webhook (Calls custom mutation webhooks)-> Validating Admission webhook (Calls custom validation webhooks)-> Custom use defined admission controllers can also be added later via manifests.Taints-> rule applied to node based on which pods are not to be scheduled there. (cause normally all nodes are welcome to host pods).-> Cases when you need to taint: GPU workloads, db workloads, infra components, control plane components.-> How a taint looks like:dedicated = database : NoSchedulegpu = true : NoScheduleWays to taint nodes:-> (Most common) kubectl taint:kubectl taint nods worker-1 dedicated = gpu : NoSchedulePage 16 (Image 16)-> directly in Node manifest (less common).apiVersion : v1kind: Nodemetadata:name: worker-1spec:taints:- key: dedicatedvalue: gpueffect: NoSchedule-> Automatically by K8s (some taints are added by controller)e.g: node.kubernetes.io/not-readynode.kubernetes.io/memory-pressure ... etc.Tolerations-> Rule on pod saying, allowing it to run on a node set not wanting taint.node set not wanting taint.-> Defined in Pod, Deployment, StatefulSet, Daemonset specification manifests.e.g: apiVersion: apps/v1kind: Deploymentspec:template:spec:tolerations- key: dedicatedPage 17 (Image 17)operator: equalvalue: gpueffect: NoScheduleNot satisfying taint -> toleration can smoke pod pending.e.g: 3 taint & tolerationNode 1 -> accept all pods (no taint)Node 2 -> tainted (gpu=true:NoSchedule)Pod 1 -> no toleration $\rightarrow$ ejectedPod 2 -> toleration $\rightarrow$ gpu=true, pod 2 allowedResult:Node 2 $\rightarrow$ Pod 2 allowed, pod 2 allowedNode 1 $\rightarrow$ Pod 1 allowed, pod 2 allowed.Affinity/Anti-affinity-> Rules before allowing pods to be placed near/force from any node/pod.-> Can have node affinity e.g: pod affinity/anti affinity.Can be hard/soft rules.Must have topology key.Node affinity-> pod placement based on node labels.e.g: if Node A $\rightarrow$ disk=sssdNode B $\rightarrow$ disk=hddThen Pod $\rightarrow$ Node Affinity :- disk = ssd. Schedule onto SSD nodes.(Continued on pg# 54)

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
