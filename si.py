import socket
import os

HOST = '172.22.80.1'  # Change this to your server's IP address
PORT = 8080

def handle_client(client_socket):
    file_name = client_socket.recv(1024).decode()
    if not os.path.exists(file_name):
        client_socket.send(b"File not found")
        client_socket.close()
        return

    client_socket.send(b"File found")

    with open(file_name, 'rb') as file:
        data = file.read(1024)
        while data:
            client_socket.send(data)
            data = file.read(1024)

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        handle_client(client_socket)

if __name__ == "__main__":
    main()
