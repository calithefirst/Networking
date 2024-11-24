import socket

# Define HOST and PORT
SERVER_HOST = "192.168.2.41"  # Replace with the server's IP address if needed
SERVER_PORT = 12345  # Port number should match the server's port
# Create the Client - Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the Server
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")

    while True:
        # Get user input and send it to the server
        message = input("Enter message for server (type 'quit' to exit): ")
        client_socket.sendall(message.encode('utf-8'))

        # If the user types 'quit', close the connection
        if message.strip().lower() == "quit":
            print("Exiting...")
            break

        # Receive a response from the server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Response from server: {response}")

except ConnectionRefusedError:
    print("Could not connect to the server. Is it running?")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the client socket
    client_socket.close()
    print("Client socket closed.")
