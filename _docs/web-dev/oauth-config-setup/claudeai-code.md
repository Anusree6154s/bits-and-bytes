---
parent: Web Dev
layout: default
date: Jan 9, 2025
permalink: claudeai-code
tags: [jwt, oauth2, typescript, nextjs, oidc, passwordless-authentication]
title: Claude AI Code for Nodemailer
hidden: true
parent_post: oauth-config-setup
---

```ts
import express from "express";
import { google } from "googleapis";
import { OAuth2Client } from "google-auth-library";
import nodemailer from "nodemailer";
import Mail from "nodemailer/lib/mailer";
import SMTPTransport from "nodemailer/lib/smtp-transport";
import {
  google_client_id,
  google_client_secret,
  google_refresh_token,
  senders_gmail,
} from "../config/constants";

const router = express.Router();

interface OTPRequest {
  email: string;
}

const createTransporter = async (): Promise<nodemailer.Transporter> => {
  try {
    const oauth2Client = new OAuth2Client(
      google_client_id,
      google_client_secret,
      "https://developers.google.com/oauthplayground"
    );

    oauth2Client.setCredentials({
      refresh_token: google_refresh_token,
    });

    const accessToken = await oauth2Client.getAccessToken();

    // Properly type the SMTP transport options
    const transportOptions: SMTPTransport.Options = {
      host: 'smtp.gmail.com',
      port: 465,
      secure: true,
      auth: {
        type: "OAuth2",
        user: senders_gmail,
        clientId: google_client_id,
        clientSecret: google_client_secret,
        refreshToken: google_refresh_token,
        accessToken: accessToken.token || undefined,
      },
    };

    const transporter = nodemailer.createTransport(transportOptions);

    // Verify transporter configuration
    await transporter.verify();
    return transporter;
  } catch (error) {
    console.error("Error creating transporter:", error);
    throw new Error("Failed to create email transporter");
  }
}

async function sendEmail(to: string, otp: string): Promise<void> {
  try {
    const transporter = await createTransporter();
    
    const mailOptions: Mail.Options = {
      from: `"Auth Service" <${senders_gmail}>`,
      to,
      subject: "Passwordless Authentication OTP",
      text: `Your OTP for authentication is: ${otp}`,
      html: `
        <h2>Authentication OTP</h2>
        <p>Use the following OTP to log in:</p>
        <h3 style="color: #4CAF50; font-size: 24px;">${otp}</h3>
        <p>This OTP will expire in 10 minutes.</p>
        <p>If you didn't request this OTP, please ignore this email.</p>
      `,
    };

    await transporter.sendMail(mailOptions);
  } catch (error) {
    console.error("Error sending email:", error);
    throw new Error("Failed to send email");
  }
}

router.post("/sendOTP", async (req: express.Request<{}, {}, OTPRequest>, res: express.Response) => {
  try {
    const { email } = req.body;
    
    if (!email) {
      return res.status(400).json({ 
        error: "Email is required" 
      });
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      return res.status(400).json({ 
        error: "Invalid email format" 
      });
    }

    const otp = Math.floor(100000 + Math.random() * 900000).toString();
    
    // Send email
    await sendEmail(email, otp);

    res.status(200).json({ 
      success: true,
      message: "OTP sent successfully" 
    });
  } catch (error) {
    console.error("Error in /sendOTP:", error);
    res.status(500).json({ 
      error: "Failed to send OTP" 
    });
  }
});

export default router;
```
