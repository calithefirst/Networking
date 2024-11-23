import socket


def start_server(host='0.0.0.0', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for 1 connection
    print(f"Server listening on {host}:{port}")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Send a confirmation message to the client
    client_socket.sendall(b"Connection successful!")
    client_socket.close()
    server_socket.close()
    print("Server closed.")


if __name__ == "__main__":
    start_server()
