---
layout: default
title: 01. Linux Basics
date: Nov 09, 2026
excerpt: Intro to kubernetes (Linux Basics)
parent: Kubernetes
permalink: kubernetes-01-linux-basics
---

## Linux Basics

<p align='center'><img src='https://github.com/user-attachments/assets/598f7ec0-caeb-4260-bb1b-6f180b0a2a79' width=100/></p>

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

