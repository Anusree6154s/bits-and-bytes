---
parent: Web Dev
layout: default
date: Jan 9, 2025
permalink: oauth-config-setup
tags: [jwt, oauth2, typescript, nextjs, oidc, passwordless-authentication]
title: OAuth Config Setup in Different Apps
excerpt: To study diff auth methods
---
# Auth App

To study diff auth methods
<br>

<video width="600" height="400" controls>
  <source src="https://github.com/user-attachments/assets/04e7f79b-77b6-4382-9507-b08ee8cdb012" type="video/mp4">
Your browser does not support the video tag.
</video>

<br>

## Notes

### Table of Contents

1. [Basic Auth](#1-basic-auth)
2. [OAuth based auth](#2-oauth)
3. [JWT token based auth](#3-jwt)
4. [Session based auth](#4-session-based)
5. [Passwordless auth](#5-passwordless)
6. [Open ID Connect (OIDC) based auth](#6-openid-connect)
7. [mTLS based auth](#7-mtls-mutual-transport-layer-security-not-implemented-completely-cause-of-minor-errors)
8. [Deployment](#8-deployment)
9. [Choice of Techstack](#9-choice-of-techstack)

<br>

### 1. Basic Auth

- Like Bearer Auth
- Using basic-auth library
- often accompanied by any other form of session/token storage to maintain session expiry

<br>

### 2. Oauth

- uses passport-google-oauth20 etc
- that uses passport session to manage sessions
- passport session needs express session
- express session can send cookies from backend to frontned (NEEDS TO BE STUDIED. NOT SURE)

  - while using diff frontend andb backend hosts only if both have https
  - only if frontend and baclemd are on same site(using nginx proxy or setting express.static())
  - _we are using express.static() method to access frontend files via backend_ [in vanilla html]

- refer [this](./oauth-oidc) for oauth apps url configurations

- **Tips**:
  - use `<base href="http://localhost:8000">` in html head to avoid rewriting baseurl in html (while accessing frontend files via backend express.static()) [in case of vanilla html]
  - use below in nextjs avoid rewriting baseurl
    ```js
    async rewrites() {
    return [
        {
        source: "/auth/:path*", // Frontend route
        destination: "http://localhost:8000/auth/:path*", // Backend route
        },
    ];
    },
    ```

<br>

### 3. JWT

- **Redis** is particularly well-suited for token blacklisting token during logout due to its speed, simplicity, and built-in expiration features. Redis is designed for low-latency operations because it stores data in memory. This makes it significantly faster than traditional disk-based databases like MongoDB or SQL.
- created redis db using upstash

<br>

### 4. Session based

- Plain session based auth
- It has already been used along with basic auth and oauth, but just t o study it in isolation

<br>

### 5. Passwordless

- Only for signup and signin. Verfication is through traditional jwt cookies/headers
- During signin we dont use password(only email). Instead would send an otp to email and verify its expiration. And then will send the token to frontend. (an extra step like 2 factor auth)
- For checking auth this token is sent via headers/stored in cookies each time for every route
- To set up modemailer follow the set mentioned here [https://dev.to/chandrapantachhetri/sending-emails-securely-using-node-js-nodemailer-smtp-gmail-and-oauth2-g3a ](https://dev.to/chandrapantachhetri/sending-emails-securely-using-node-js-nodemailer-smtp-gmail-and-oauth2-g3a ) and code mentioned in claude ai code here [claudeai-code.md](./claudeai-code)

<br>

### 6. OpenID Connect

- We used Google as the OpenID Provider (IdP) and passport-openidconnect to help set up openid

<br>

### 7. mTLS (Mutual Transport Layer Security) (not implemented completely cause of minor errors)

- [https://github.com/edum-compassuol/mTLS-nodejs-example/blob/main/server/src/server.ts](https://github.com/edum-compassuol/mTLS-nodejs-example/blob/main/server/src/server.ts)
- Mutual TLS (mTLS) authentication involves verifying both the client and server identities using TLS certificates.
- Includes 2 steps:
  1. creating certficated for server & client
  2. logging in after verifying the certificates (session is managed by header/cookies)
- First You'll need to create the following in a seperate folder called `cert` outside frotend or backend folder:
  - A CA certificate to sign client and server certificates.
  - A server certificate and private key.
  - A client certificate and private key.
- Download ssl from [https://slproweb.com/products/Win32OpenSSL.html](https://slproweb.com/products/Win32OpenSSL.html)
- OpenSSL commands to create certificates in cert folder: [ssl-commands.md](./ssl-commands)
- **remember to add the folder cert/ and all the related certificate extensions as in [gitignore-commands.md](./gitignore-commands) to gitignore before committing**
- If everything is configured correctly:
  - The server will verify the client certificate.
  - The client will verify the server certificate.
- Common Issues
  - Certificate Mismatch: Ensure the client and server - certificates are signed by the same CA.
  - Incorrect Paths: Double-check the file paths for the keys and certificates.
  - Firewall/Port Issues: Ensure port 8443 is open for communication.(convetionally use port 8443 for mTLS)
- Used in Banks (e.g., JPMorgan Chase, Goldman Sachs), Payment Processors (e.g., Stripe, PayPal, Square), Cloud Providers (e.g., AWS, Microsoft Azure, Google Cloud), etc
- Working:
  - Browsers do not natively support mTLS directly due to security constraints. So we will use nextjs api to work with client certificates. (∴ cannot do directly within page.tsx)

<br>

### 8. Deployment

- Basic typescript nodejs deployment: [https://youtu.be/4mqy5SjkDec?si=rFG2Wu8NYmq-8PjD](https://youtu.be/4mqy5SjkDec?si=rFG2Wu8NYmq-8PjD)
- Durig deployment, there is this whole mess. Checkout all changes I've made so far, all the minor fix commits to get an idea.
- Express session does indeed not work with frontend and backend on diff servers.
  - During development it worked because the browser confused the host(localhost) of both port 8000 and 3000 as it is coming from same domain.
  - Added diff frontend host url as below in .env file of react to change hostname and it stopped co-operating with express-session
  ```bash
  HOST=frontend.local
  ```
  - Therefore had to serve rthe frontend build folder from backend
- Render is horrible at building and starting the server by itself for frontend as well as backend (as I've seen so far).
  - Therefore I'm building the build files in both frontend and backend before commiting and pushing the build folders to github
  - In render I just start the backend server
- Rememeber for OAuth authentication always need to update the redirect urls in case you plan to host the server in any other website.
  - Also update the env variables accordingly

<br>

### 9. Choice of Techstack

- ReactJS because of not able to use express-session
  - NextSJ was the first choice in order to learn the techstack. But express-session was not letting me set cookies in frontend because of cross-origin. (couldnt find a simple solution in neither stackoverflow nor gpt)
  - So now im serving react build files directly from server
