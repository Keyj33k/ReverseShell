#!/usr/bin/env python3
class silentHill:

    def __init__(self):
        self.LISTEN_ADDRESS = "127.0.0.1"
        self.LISTEN_PORT = int(4444)
        import socket
        try:
            sock = socket.socket()
            sock.bind((self.LISTEN_ADDRESS, self.LISTEN_PORT))
            sock.listen(1)
            print(f"[*] Listening on {self.LISTEN_ADDRESS}:{self.LISTEN_PORT}")
            client = sock.accept()
            print(f"[*] Client connected {client[1]}")
            sock.close()
        
        except Exception as ERROR:
            from termcolor import colored
            import sys
            print(colored("An error was defined!", "red"))
            print(ERROR)
            sys.exit(1)

if __name__ == "__main__":
    silentHill()
