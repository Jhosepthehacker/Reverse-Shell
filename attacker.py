import socket

class SocketReverseShellAttack:
    def __init__(self):
        self.HOST = host
        self.PORT = port

    def receive_connection:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen(5)

            while True:
                conn, addr = s.accept()
                print(f"Conección establecida con: {conn}:{self.PORT}")
