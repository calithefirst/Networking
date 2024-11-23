import socket


def start_client(server_ip, port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))
    print(f"Connected to server at {server_ip}:{port}")

    # Receive the confirmation message from the server
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Message from server: {message}")

    client_socket.close()
    print("Client closed.")


if __name__ == "__main__":
    server_ip = input("Enter the server's IP address: ")
    start_client(server_ip)
