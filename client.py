import socket

# Server IP and port
SERVER_IP = "172.23.0.1"
SERVER_PORT = 12345

def main():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    
    print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")
    
    while True:
        message = input("Enter your message: ")
        
        # Send the message to the server
        client_socket.send(message.encode())
        if message.lower() == "bye":
            break
        
        # Receive and display the server's response
        response = client_socket.recv(1024).decode()
        print(f"Server says: {response}")
    
    client_socket.close()
    print("Connection closed")

if __name__ == "__main__":
    main()
