import socket

# Add suspicious IP addresses here
suspicious_ips = {"10.30.201.84"}

def block_suspicious_client(client_socket, client_address):
    if client_address[0] in suspicious_ips:
        client_socket.send(b"You are blocked.")
        print(f"Suspicious IP address {client_address[0]} is blocked.")
        return True
    return False

def handle_client(client_socket, client_address):
    if block_suspicious_client(client_socket, client_address):
        client_socket.close()
        return

    print(f"Connection established with {client_address[0]}:{client_address[1]}")
    # Your server logic here

if __name__ == "__main__":
    server_ip = "0.0.0.0"  # Listen on all available interfaces
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print("Server is listening for connections...")
    while True:
        client_socket, client_address = server_socket.accept()
        handle_client(client_socket, client_address)
