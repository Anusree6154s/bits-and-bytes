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
    - rwx r-x r--
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

<p align='center'><img width=100 src='https://github.com/user-attachments/assets/aaa7d857-4270-44f8-a848-9b834f0c1b53' /></p>

- Problem — containers crashing 
- K8s solution = self-healing 
- Explanation 
    - K8s continuously watches containers 

    $\star$ K8S visualization A data center looks like this
- Datacenter   - Rack   - Server 1   - Server 2   - Server 3   - Rack   - Server 4   - Server 5   - Server 6   - Different servers on diff racks can be part of same Kubernetes cluster.   - When multiple servers have cost check, certain requirements, they are as associated of k8s, they are then part of k8s cluster.   - Requirements to be part of k8s cluster:-   $\star$ K8s terms   kubelet   - small local agent/process   - Exists on every worker node / control plane node.   - Make sure containers/pods runs correctly on that m/c.   Image 11- Tasks of kubelet :- talk to api server, receive pod assignments, start/stop containers, report node health, report pod status, mounts volume, handle probes.   kubelet   - Pronounced "kyoo-belet" or "kyoo-be-control".   - Exists on developer laptop / admin m/c / control server.   - It communicates of kube-apiserver.   kube-proxy   - Kubernetes n/w proxy.   - exists on every worker node (as daemon/fbg process).   - It handles k8s n/wing rules inside cluster   Eg: Service virtual IPs, load balancing, traffic forwarding, ip tables / ipvs rules.   Node   - Physical servers or VM running linux, kubelet or container runtime.   kubeadm   - K8s admin / bootstrap tool   Image 12- exists on control plane m/c.   - worker setup m/c   - used during cluster creation for creating control plane "kubeadm init" & join worker pods "kubeadm join", etc...   - Not part of ras running cluster logic instead part of cluster installation / setup tool.   kube-apiserver   - main entry point for k8s cluster.   Everything talks to this.   Acts like central management api.   - Exists on control plane server.   - Talks to kubectl, kubelet, scheduler, controller-manager, etcd.   kube-scheduler   - chooses which node runs pods.   (decision engine)   - Exists on control plane server.   Chooses where worker node try maintains desired state pods.   - talks to kube-apiserver, worker nodes indirectly.   Image 13- kube-controller-manager   - Exists on control plane server.   - Maintains desired state.   - Talks to :- kube-apiserver, etcd ... indirectly.   - Runs reconciliation loops (loops inside k8s that continuously check desired state vs actual state).   - eg: desired replica = 3, actual replica = 2. Then create another pod.   etcd (etc distributed) (ct-see-di)   - etcd dictionary / distributed db (like redis)   - store cluster state db.   - most critical k8s db (source of truth).   - Exists on control plane servers.   - Stores :- pods, deployments, services, [as key-value pairs] nodes, secrets, cluster desired state.   $\star$ distributed   it is called distributed bcoz multiple etcd servers can work together.   [Continued containerized]   (actually runs containers)   - container runtime (actually runs containers)   - Exists on worker node.   - Talks to kubelet through CRI.   eg if multiple control planes with diff etcd, they communicate via "consensus" algorithm which stores a copy of the...   Image 14   - [.. exists on worker node - talks to kubelet through CRI with diff etcd, they communicate via consensus algorithm which stores a copy of the cluster state, thus preserving data even if one etcd beads down. (cluster state is not the same as control plane).   CoreDNS (Core Domain Name Sys)   - K8s   - Internal cluster dns.   - lets pods communicate using names.   eg: api-service.default.svc.cluster.local.   - usually runs as pods on worker nodes.   Container Network Interface (CNI)   - Provide pod networking.   - Exists as CNI plugins on worker nodes.   - eg: Calico, Flannel, Cilium.   CRI   - Container runtime interface. (node agent)   - Standard interface btw. kubelet & container runtime (containerd).   - Types of communication being done via here include kubelet asking to pull image, start container, stop container, delete container, get container status, etc..   CSI   - Container storage interface.   - Standard way k8s interact w/ storage systems.   
