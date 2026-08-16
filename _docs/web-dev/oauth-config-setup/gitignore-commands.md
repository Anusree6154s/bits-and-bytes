---
parent: Web Dev
layout: default
date: Jan 9, 2025
permalink: gitignore-commands
tags: [jwt, oauth2, typescript, nextjs, oidc, passwordless-authentication]
title: Gitignore Config for Certificates
hidden: true
parent_post: oauth-config-setup
---

```.gitignore
# config specific to the language or editor you use

# Ignore certificate and key files
*.key
*.crt
*.csr
*.pem
*.p12
*.der
*.srl

# Ignore any directory containing certs or keys
certs/
keys/
secrets/
```
