#!/usr/bin/env python3

# # # # # # # # # # # # # # # # # # # # # #
#                                         #
#   Author  :   Keyj33k                   #
#   Contact :   nomotikag33n@gmail.com    #
#   Twitter :   @keyjeek                  #
#   Github  :   @keyj33k                  #
#   Version :   1.0.0                     #
#                                         #
# # # # # # # # # # # # # # # # # # # # # # 

class silentHill:

    def __init__(self):
        self.LISTEN_ADDRESS = "127.0.0.1"
        self.LISTEN_PORT = int(4444)
        import socket
        try:
            SOCKET_SOCK = socket.socket()
            SOCKET_SOCK.bind((self.LISTEN_ADDRESS, self.LISTEN_PORT))
            SOCKET_SOCK.listen(1)
            print(f"[*] Listening on {self.LISTEN_ADDRESS}:{self.LISTEN_PORT}")
            client = SOCKET_SOCK.accept()
            print(f"[*] Client connected {client[1]}")
            SOCKET_SOCK.close()
        
        except Exception as ERROR:
            from termcolor import colored
            import sys
            print(colored("An error was defined!", "red"))
            print(ERROR)
            sys.exit(1)

if __name__ == "__main__":
    silentHill()
