---
layout: default
title: Load Balancing And Traffic Management
permalink: load-balancing
date: Nov 11, 2026
excerpt: Understanding Load Balancing
parent: Load Balancing And Traffic Management
---

# load balancing

- Round robin
  - load distributed sequentially & evenly across available servers.
  - Eg:
  ```
  upstream backend {
      server app1 : 3000;
      server app2 : 3000;
      }
  ```
- weighted load balancing
  - you weight servers. % wise
  - Eg:
  ```
  upstream backend {
      server app1 : 3000
      weight = 3;
      server app2 : 300
      weight = 1;
      }
  ```

  - app 1 get 75% more traffic.
- least connections
  - traffic to least busy instance.
  - Eg:
  ```
  upstream backend {
      least_conn;
      server app1 : 3000;
      server app2 : 3000;
      }
  ```
- Health check/failover
  - if app dies, traffic moves to app2.
  - Eg:
  ```
  upstream backend {
      server app1 : 3000
      max_fails = 3
      fail_timeout = 30s
      server app2 : 3000;
      }
  ```
- sticky session load balancing
  ```
  upstream backend {
      ip_hashserver ...
      }
  upstream backend {
      sticky cookie srv_id expires = 1h;
      server apps ...
      }
  ```

  - can be based on IP or cookies etc.
  - not a load balancing algo, but rather a constraint that modifies load balancing behaviour.
