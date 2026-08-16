---
title: Vercel .env extraction
excerpt: Extracting environment variables from deployed vercel app
date: 27 Feb 2025
permalink: vercel-env
tags: [vercel, env]
layout: post
---

## Vercel Env Variable Extraction

To extract environment variables from an app deployed in vercel, from vercel to our local IDE, we just have to do the following:
  1. Open the respective app in your IDE
  2. run `vercel pull` and link with your existing deployed vercel app
  3. run `vercel env pull .env` or `vercel env pull .env.local`

  The env variables will appear in your IDE in a dedicated file easily!
