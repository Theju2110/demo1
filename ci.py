import socket

HOST = '172.22.80.1'  # Change this to your server's IP address
PORT = 8080

def send_file(file_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    with open(file_name, 'rb') as file:
        client_socket.send(file_name.encode())

        response = client_socket.recv(1024)
        if response == b"File not found":
            print("File not found on the server")
            client_socket.close()
            return

        with open(f"received_{file_name}", 'wb') as received_file:
            data = client_socket.recv(1024)
            while data:
                received_file.write(data)
                data = client_socket.recv(1024)

    client_socket.close()
    print("File transfer successful")

def main():
    file_name = input("Enter the name of the file to send: ")
    send_file(file_name)

if __name__ == "__main__":
    main()
