---
parent: Web Dev
layout: default
date: Jan 9, 2025
permalink: oauth-oidc
tags: [jwt, oauth2, typescript, nextjs, oidc, passwordless-authentication]
title: OAuth/OIDC App Configurations
hidden: true
parent_post: oauth-config-setup
---

# OAuth/OIDC App Configurations

### Table of Contents
1. [OAuth config](#oauth-configuration)
    1. [Google](#google-oauth)
    2. [Facebook](#facebook)
    3. [Twitter](#twitter)
    4. [Github](#github)
2. [OIDC config](#oidc-configuration)
   1. [Google](#google-oidc)

   
## OAuth Configuration

### Google OAuth
1. visit https://console.cloud.google.com/
   - <img width="400" alt="image" src="https://github.com/user-attachments/assets/f4118bef-c176-47af-9dfe-1d70f8672e2f"/> 
3. add project/choose project
    - add project
        - <img width="300" alt="image" src="https://github.com/user-attachments/assets/5bdb6739-ad8f-4986-b13e-b882ddcc19a5" />
        - <img width="400" alt="image" src="https://github.com/user-attachments/assets/3e3741c1-a5ae-4fd7-a93e-5d8b5a1dc878" />
        - <img width="400" alt="image" src="https://github.com/user-attachments/assets/6c3f61ca-55f3-49bb-8123-5c70caaecbb3" />
        - fill oauth consent screen. keep setting same in all. just change names wherever neccessary. fill those place that are filled
            - <img width="300" alt="image" src="https://github.com/user-attachments/assets/92473ec7-6e6c-40e0-a094-9ed377d260d1" />
            - <img width="400" alt="image" src="https://github.com/user-attachments/assets/cb4d8375-c38a-4ee8-bcca-312678d37d26" />
            - <img width="400" alt="image" src="https://github.com/user-attachments/assets/c7653316-4e71-412c-a029-bec9c0fc12f2" />
    - or choose project
    - <img width="400" alt="image" src="https://github.com/user-attachments/assets/999366b0-f8fb-4fec-995b-2aad27529eee" />
4. add credentials
   - <img width="200" alt="image" src="https://github.com/user-attachments/assets/acf3044d-2c89-41e9-b2b2-b223ee0e0602" />
   - <img width="400" alt="image" src="https://github.com/user-attachments/assets/acbe9869-2959-4847-b10d-d6fd2506f34b" />
   - getting google api key for apps like nodemailer
       - <img width="400" alt="image" src="https://github.com/user-attachments/assets/48996fca-30f0-4f64-a6df-36d934e57517" />
       - <img width="400" alt="image" src="https://github.com/user-attachments/assets/a6a7037f-3b20-4191-a319-5ce0b408ebe1" />
   - getting google cient id and secret for oauth
       - <img width="500" alt="image" src="https://github.com/user-attachments/assets/d6aa41a8-a35d-46a2-8f0e-98dff4632fab" />
       - <img width="500" alt="image" src="https://github.com/user-attachments/assets/ee9a6e10-18cd-4364-9c67-4d7817aa606b" />
       - <img width="500" alt="image" src="https://github.com/user-attachments/assets/ae7f9b61-8621-4b15-acb4-feffba10d8d5" />
       - <img width="300" alt="image" src="https://github.com/user-attachments/assets/9d355a62-decf-4fef-b312-f17e2ab23f52" />
5. adding redirect uris and source url (needs to be changed each time you change hostname or create a new deployment url)
   - <img width="400" alt="image" src="https://github.com/user-attachments/assets/ed9bde68-6c83-4ca7-b319-ee38574acdd1" />

### Facebook
1. visit facebook developer portal https://developers.facebook.com/
    - <img width="600" alt="image" src="https://github.com/user-attachments/assets/1f69d3c0-2494-41b2-aac1-cee03118cacc" />
3. create a new app/choose existing app
    - create new app
    - <img width="600" alt="image" src="https://github.com/user-attachments/assets/c53caf90-f6a3-4de1-8e75-f93001b1d383" />
    - <img width="400" alt="image" src="https://github.com/user-attachments/assets/5067b56f-d3ca-4d12-9459-63bdf4d569fc" />
    - <img width="600" alt="image" src="https://github.com/user-attachments/assets/edc41216-1066-4ffc-9b71-2267b9e3a3e7" />
    - <img width="400" alt="image" src="https://github.com/user-attachments/assets/25cca23d-a911-492c-bf9c-3f745ac076ab" />
    - <img width="432" alt="image" src="https://github.com/user-attachments/assets/0f878b3d-02ba-4ba4-886a-fa99fea6b024" />
    - <img width="430" alt="image" src="https://github.com/user-attachments/assets/29d2c4b8-34fe-46be-906f-0ed3cf450124" />
    - <img width="212" alt="image" src="https://github.com/user-attachments/assets/c12339ef-5b45-4ba1-83b3-89734779f878" />
- NOT COMPLETED BECAUSE I DONT KNO WHY BUT APP IS WORKING NO MATTER WHAT CHANGE I MAKE

### Twitter

- <img width="600" alt="image" src="https://github.com/user-attachments/assets/596f9791-9eae-483f-9a14-9bc49391d99f" />
- <img width="400" alt="image" src="https://github.com/user-attachments/assets/0c4c1cbe-4f9f-41ab-9a96-970c0dc387df" />
- <img width="400" alt="image" src="https://github.com/user-attachments/assets/5ce047e0-42f1-4f88-af39-293615133007" />
- <img width="300" alt="image" src="https://github.com/user-attachments/assets/d84544ad-4eab-4504-9f75-848b0170487d" />
- <img width="300" alt="image" src="https://github.com/user-attachments/assets/67e867dd-327f-428c-8557-d19a1bb80a11" />
- <img width="600" alt="image" src="https://github.com/user-attachments/assets/983f6cd8-4c62-405c-95c7-cb478324fc02" />
- <img width="300" alt="image" src="https://github.com/user-attachments/assets/431f9c14-5afd-4220-8949-6646ae36d287" />
- <img width="300" alt="image" src="https://github.com/user-attachments/assets/db41f022-39e3-465d-9d2b-edbeb8c95f0a" />
- <img width="400" alt="image" src="https://github.com/user-attachments/assets/05e79721-938d-4de5-b447-4b7bdeb3257f" />
- <img width="400" alt="image" src="https://github.com/user-attachments/assets/7fbe7571-a483-45c3-bf0c-1a3cc85e21f8" />


### Github
- <img width="300" alt="image" src="https://github.com/user-attachments/assets/c495dd2f-a80c-43c3-a068-9b78ebe820cc" />
- <img width="200" alt="image" src="https://github.com/user-attachments/assets/33f8a77d-2ff0-47ff-bec8-eade05ce381c" />
- <img width="200" alt="image" src="https://github.com/user-attachments/assets/d0a9920d-1cfc-4679-b5ce-80b9ec03e991" />
- <img width="200" alt="image" src="https://github.com/user-attachments/assets/f9e08de4-3ad5-49ff-91be-8a1f95f77d4f" />
- <img width="600" alt="image" src="https://github.com/user-attachments/assets/793ca42d-bef2-4e83-a504-cdedabbdc925" />
- <img width="300" alt="image" src="https://github.com/user-attachments/assets/27169d01-91f2-4416-b8a5-221248a19d1e" />
- <img width="600" alt="image" src="https://github.com/user-attachments/assets/28e7561b-7f06-4901-877b-dc1efe4ab58d" />
- <img width="600" alt="image" src="https://github.com/user-attachments/assets/ccfc0e2f-3246-4ef2-bdd1-8a28cc6b196d" />

## OIDC Configuration
### Google OIDC
- follow all same steps as in [google oauth](#goggle-oauth), except the last step - just callback url is different
    - <img width="400" alt="image" src="https://github.com/user-attachments/assets/1cbf5d6d-dc88-4aab-9a82-61e10ed305e6" />
