import socket
import select

# Server IP and port
SERVER_IP = "192.168.43.205"
SERVER_PORT = 12345

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the server IP and port
    server_socket.bind((SERVER_IP, SERVER_PORT))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")
    
    # List of sockets for select
    sockets_list = [server_socket]
    
    while True:
        # Use select to wait for incoming data and connected sockets
        read_sockets, _, _ = select.select(sockets_list, [], [])
        
        for socket_item in read_sockets:
            if socket_item == server_socket:
                # New client connection
                client_socket, client_address = server_socket.accept()
                print(f"Connected to {client_address}")
                
                # Add the new client socket to the list
                sockets_list.append(client_socket)
            else:
                # Existing client sending data
                try:
                    # Receive data from the client
                    data = socket_item.recv(1024).decode()
                    
                    if not data:
                        # Client closed the connection
                        print(f"Connection closed with {client_address}")
                        socket_item.close()
                        sockets_list.remove(socket_item)
                        continue
                    
                    print(f"Received from {client_address}: {data}")
                    
                    if data.lower() == "bye":
                        response = "Goodbye"
                        socket_item.send(response.encode())
                        socket_item.close()
                        sockets_list.remove(socket_item)
                    else:
                        # Send response to the client
                        response = input("Enter your response: ")
                        socket_item.send(response.encode())
                except Exception as e:
                    # Client encountered an error, close the connection
                    print(f"Error with {client_address}: {e}")
                    socket_item.close()
                    sockets_list.remove(socket_item)

if __name__ == "__main__":
    main()
