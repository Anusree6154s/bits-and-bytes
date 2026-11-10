---
layout: default
title: SSE vs Websocket
permalink: sse-vs-websocket
date: Nov 11, 2026
excerpt: Understanding diff b/w SSE and Websocket
parent: Networking And Protocols
---

# SSE vs Websocket

> (Rest api still always better than these open connections)

- SSE
  - Server sent events.
  - way for server to continuously push updates to a client via HTTP. one-way
  - switch (notification, live dashboard, logs, tokens)
- Web socket
  - continuous message from both client and server.
- both use an open connection (not polling). SSE uses HTTP connection. websocket starts as HTTP and then upgraded to websocket protocol where messages are exchanged as websocket frames.
  (chat apps, game, collab editing)
