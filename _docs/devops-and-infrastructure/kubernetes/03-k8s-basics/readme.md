---
layout: default
title: 03. K8s Basics
date: Nov 09, 2026
excerpt: Intro to kubernetes (K8s Basics)
parent: Kubernetes
permalink: kubernetes-03-k8s-basics
---

## K8s Basics

So we are back to continuing with k8s basics dropping media forge in between 🥲🙂

### Linux Basics
<p align='center'><img src='https://github.com/user-attachments/assets/5d427eea-59c2-4acb-a328-8c0f64f38729' width=100/></p>

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

<p align='center'><img src='https://github.com/user-attachments/assets/5b38a59f-359a-4887-b8ea-2436179994c9' width=100/></p>


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

<p align='center'><img src='https://github.com/user-attachments/assets/37a2415d-14c5-42c5-b21d-0ada0eef8552' width=100/></p>

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
    - Process of CNI working (what all CNI does)   
      - when a new pod starts   
        - CNI allocates an IP   
        - create network interface   
        - configure routing   
        - connect pod to cluster N/W.   
    - Points to note:   
      - CNI (container n/w interface) is a specification, by a set of plugins.   
      - it creates/configures n/working for containers & pods.   
      - CNI plugin is a plugin that resides on every K8s node. It is an executable file. unlike API objects or controllers, which create/configure upon running the file.   
      - It doesn't generally come with K8s cluster when we create one. A ductii controllers and such. A administrator generally need to set it up.   
      - Commonly installed CNI plugins :- Calico, Cilium, Flannel.   Page 2(2)   
      - But many providers provide auto installs, many things for developers thus it may feel like built in.   
      - Providers that auto installs include :- minikube kind, EKS, GKE, AKS.   DNS Resolution - convert name into IP addresses.
- Phase 7 - Resource management   
  - Requests :
    - to declare minimum resources required (pod-level)   
    - eg: 
    ```
    requests:
      cpu: 500m
      memory: 512Mi
    ```
    - this means: pods node needs 0.5 CPU & 512 MB RAM.   
  - Limits :
    - to declare maximum resources allowed.   
    - eg: 
    ```
    limits:
      cpu : 1
      memory : 1Gi
    ```
    - which means node needs max 1 CPU & 1 GB RAM   
  > For nodes, resources are allocated via "capacity" and "allocatable resources"   To decide placement of pods in nodes, scheduler adds the requests & limits of pods/containers & then compares with node allocatable capacity  
  - cpu throttling
    - Prevent containers from exceeding CPU limits
    - Process :
      - Developer sets CPU limit   
      ````
      limits :
        cpu : 1"  
      ```
      - kubelet reads pod spec.   
      - Container runtime configures cgroups.   
        - runtime creates linux cgroup setting for container   
      - linux kernel tracks cpu usage by watching how much CPU time certain cgroup consumes.   
      - Container reaches its quota C like if cpu is 1; but container consumes 100ms of cpu time (quota) every 100 ms window (period).   
      - Kernel throttles.   
        - kernel blocks further cpu execution. Container waits until the next period begins. (means process is either killed nor pod is contacted. Process sleeps.)   
    - OOM killed   
      - out of memory killed   
      - purpose is to protect node from memory exhaustion   
      - When RAM usage exceeds by containers, kernel kills the containers process. Then the pod may be restarted   
    > **Note**   
    > cpu limit exceed -> process only steps (Throttle)   
    > memory limit exceed -> process killed (oom)   
    
    - scheduling   
      - K8s scheduler choosing which node will run the pod.   
    - Node Pressure:   
      - Purpose is to detect overloaded nodes   
      - Common pressure types:   Memory pressure, disk pressure, PID pressure.   
      - e.g. K8s servers have RAM = 128 GB, used RAM = 127 GB   
        - node enters memory pressure   
        - K8s may evict nodes to protect the node.   
      > If no free nodes 10% full memory exists on the cluster, then the   Page 5exists on the cluster, then the new pod goes into pending state   (In case of fixed replicaset with stateless deployment pods)   
