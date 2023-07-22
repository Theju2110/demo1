import socket

def connect_to_server(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket

if __name__ == "__main__":
    server_ip = "10.30.201.84"  # Change this to your server IP
    server_port = 12345

    client_socket = connect_to_server(server_ip, server_port)

    response = client_socket.recv(1024).decode()
    print("Server response:", response)

    client_socket.close()
