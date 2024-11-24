import socket

# Define the HOST and Port
HOST = ""  # Listen on all network interfaces, also with NONE or "0.0.0.0"
PORT = 12345  # Arbitrary port number (>1024)

# Socket creation (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Configure the Socket -> bind, listen
server_socket.bind((HOST, PORT))  # bind the socket to address
server_socket.listen(1)  # start listening with a queue of up to 5 connections

print(f"Server listening on {HOST}:{PORT}")
print(server_socket)

# Accepting Incoming Connections
while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    try:
        while True:
            # Receive a message from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print("Client disconnected")
                break
            print(f"Message from {client_address}: {data}")

            # Respond to the client (optional)
            client_socket.sendall(b"Message received: " + data.encode('utf-8'))

            # If the client sends 'quit', break out of the loop
            if data.strip().lower() == "quit":
                print("Client requested to terminate the connection.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        client_socket.close()
        print(f"Connection with {client_address} closed.")
