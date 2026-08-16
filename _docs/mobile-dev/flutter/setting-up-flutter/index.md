---
layout: default
title: Flutter Setup Guide
date: Jul 13, 2025
excerpt: Guide to setting up flutter in vs code
permalink: setting-up-flutter
tags: [flutter, dart, mobile, android, ios]
parent: Flutter
---

I have been looking on how to create my own gujrati learning app and thought, well why not learn something that's used in my office. And so I chose flutter. <img src="{{ '/assets/imgs/setting-up-flutter.png' | relative_url }}" width=30 height=30/>

Now I was used to using vs code. So went and prompted gpt to help me set up flutter in vs code, and this is its response that worked well for me:

<br>

<div style="border:1px solid #ccc; padding:10px; border-radius:5px"  markdown="1">

### 🚀 Flutter Development with **VS Code**

- #### ✅ 1. **Install Prerequisites**

  - ##### 📦 Flutter SDK

    - Go to: [https://docs.flutter.dev/get-started/install](https://docs.flutter.dev/get-started/install)
    - Download for your OS (Windows/Linux/macOS)
    - Extract and add the `flutter/bin` folder to your **system PATH**

    > **To verify installation:**

    ```bash
    flutter --version
    ```

  - ##### 💻 Install VS Code

    - Download: [https://code.visualstudio.com/](https://code.visualstudio.com/)

  - ##### 🧩 Install Extensions in VS Code

    1.  Open VS Code
    2.  Go to Extensions (`Ctrl+Shift+X`)
    3.  Install these:

        - ✅ Flutter (by Dart Code)
        - ✅ Dart (automatically gets installed with Flutter)

  - ##### 📱 Install Android Studio (for Android SDK & Emulator)

    - You don’t need to use Android Studio, but you **do need** its SDK + emulator

    1.  Install: [https://developer.android.com/studio](https://developer.android.com/studio)
    2.  During setup, **check**: Android SDK + Emulator
    3.  After install, open Android Studio > Preferences > SDK Manager

        - Ensure **Android SDK**, **platform tools**, and at least one **API version** are installed

    > **For emulator**:

    - Create one using AVD Manager inside Android Studio
    - Or use a **real Android device** in developer mode + USB debugging

- #### ⚙️ 2. **Check Flutter Environment**

  Run:

  ```bash
  flutter doctor
  ```

  ✅ It should show checkmarks for:

  - Flutter
  - Dart
  - Android toolchain
  - VS Code
  - (iOS only if on macOS)

- #### 📁 3. **Create a New Flutter Project**

  In terminal or VS Code terminal:

  ```bash
  flutter create my_app
  cd my_app
  code .    ## opens the project in VS Code
  ```

- #### 👨‍💻 4. **Run Your App**

  1. Connect your Android device or start an emulator
  2. In terminal:

     ```bash
     flutter run
     ```

  Or use **F5** in VS Code to launch the debugger.

- #### 📂 5. **Start Coding**

  - Your main file: `lib/main.dart`
  - Modify the default code or replace with your own UI

- #### 🔁 6. **Hot Reload / Restart**

  - Save file to see changes instantly (**hot reload**)
  - Use `r` or `R` in terminal when app is running
  - Or use the **Flutter toolbar** in VS Code

#### 🛠 Optional: Android App Icon & Name

- Edit in `android/app/src/main/AndroidManifest.xml`
- Use package: [`flutter_launcher_icons`](https://pub.dev/packages/flutter_launcher_icons)

</div>
