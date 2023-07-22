import socket

# Server IP and port
SERVER_IP = "172.23.0.1"
SERVER_PORT = 12345

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the server IP and port
    server_socket.bind((SERVER_IP, SERVER_PORT))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")
    
    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")
        
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            
            if not data:
                break
            
            print(f"Received from {client_address}: {data}")
            
            if data.lower() == "bye":
                response = "Goodbye"
                client_socket.send(response.encode())
                break
            
            # Send response to the client
            response = input("Enter your response: ")
            client_socket.send(response.encode())
        
        client_socket.close()
        print(f"Connection closed with {client_address}")

if __name__ == "__main__":
    main()
