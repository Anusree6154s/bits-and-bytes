---
layout: default
title: LXC
date: Nov 10, 2026
excerpt: Understanding Linux Containers (LXC)
parent: Devops And Infrastructure
permalink: lxc
---

# LXC (Linux containers)

- facts
  - OS-level virtualisation - Not hardware virtualisation.
  - Runs in containers on a host linux kernel.
  - Acts like a small linux m/c.
  - system container (like how docker is application container)
  - Every container has its own - PID namespace, n/w namespace, mount namespace, hostname, filesystem, users (optionally mapped).
  - Containers are isolated using linux namespace and cgroups.
  - linux cgroups enforces following limits on lxc container: RAM, CPU cores, CPU time, disk quota, w/o bandwidth, I/O limits.
  - Has singe host ckernles the kernel. Cannot boot a diff kernel inside lxc like windows on FreeBSD.

  ```
  host ubuntu kernel
          |
  -----------------
  |               |
  v               v
  lxc 1          lxc 2
  (ubuntu)       (debian)
  ```

- Performance (Compared to VMs):
  - Faster startup, lower RAM overhead, better density (more containers per host).
- Persistence:
  - Stays stuff installed on exe container remains installed even after reboot (less compared to VMs, bcz host kernel is shared).
- Security:Less vulnerability can affect all containers.
- Limitation:
  - Linux guests only, cannot use different kernel version, some kernel features/modules depend on host; certain workloads (eg: some K8s or nested containers scenarios) may require extra configuration as workloads in VMs in K8s.
