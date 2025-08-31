
### Note

- Process of re-setting up project locally
  - **Install ruby**:
    - [https://rubyinstaller.org/](https://rubyinstaller.org/)
    - Download the latest **Ruby+Devkit** version for Windows.
    - GPT asked to do this: `Install with all defaults, and check the box that says "Add Ruby executables to your PATH".`. But couldn't do it and nothing went wrong
    - After install, it may ask to run `ridk install`. Choose option `3` (install MSYS2, MINGW, etc.).
  - **Install Bundler**
    - Open command prompt (not bash terminal)
    - Run `ruby -v` and `gem install bundler`
    - Get the location fo ruby by running `where ruby`. If path is `C:\Ruby34-x64\bin\ruby.exe` then run this in bash terminal to add the bath to `.bashrc`:
      ```
      echo 'export PATH="/c/Ruby34-x64/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc
      ```
  - **Run bundler in bash**
    - In terminal, run `bundle install` and `npm start`
- Process of committing and deploying app
  - Commit changes to main branch
  - Upon pushing code to main, github workflows will atomatically push lastest changes to gh-pages branch and deploy the latest commit from there
