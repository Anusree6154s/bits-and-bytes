---
parent: Web Dev
layout: default
date: Jan 9, 2025
permalink: ssl-commands
tags: [jwt, oauth2, typescript, nextjs, oidc, passwordless-authentication]
title: SSL Commands
hidden: true
parent_post: oauth-config-setup
---

Generate a CA certificate:

```bash
openssl genrsa -out ca.key 2048
openssl req -x509 -new -nodes -key ca.key -sha256 -days 365 -out ca.crt
```

Generate a server certificate:

```bash
openssl genrsa -out server.key 2048
openssl req -new -key server.key -out server.csr
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365 -sha256
```

Generate a client certificate:

```bash
openssl genrsa -out client.key 2048
openssl req -new -key client.key -out client.csr
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt
```
