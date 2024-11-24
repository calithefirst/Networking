Shortcuts:
Replace Words: <CTRL> + <SHIFT> + <R>


1. Terminal User Interface (TUI)
    - Build own CLI 'Tools'
    - main() command line args


2. Socket
    - ip address and port number
    - using TCP/IP protocol


Notes:

### Socket Programming ###

Chapter 1: Understanding Socket Module

- socket module in python provides low-level networking interfaces
- enabling communication over TCP or UDP
- abstracts the complexities of raw socket programming
    -> making it easier to create networked applications


Chapter 2: Core Features of the socket module

1. Host Address and Port Number

1.1 Host Address:
    - the host address defines the interface the server listens on
    - Possible Interfaces:
        - ...

1.2 Port Number:
    - the port number identifies the specific application or service on the host
    - Valid port range from 1 to 65535. Port ranges:
        - Port 0-1023:
        - Port 1024-49151:
        - Port 49152-65535:
Note: When defining a host and port, you provide them as a tuple: (host, port)


2. Socket Creation
-> Create a socket object using socket.socket() and specify:
    - Address Family: e.g. AF_INET for IPv4 or AF_INET6 for IPv6
    - Socket type: e.g. SOCK_STREAM for TCP or SOCK_DGRAM for UDP
Note: see python docs for more Information for specifying the Socket

Example:
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


3. Socket Configuration

### Server ###
a) Binding and Listening
    - the server binds to an IP address and port using bind()
    - the server listens for incoming connections using listen()

b) Accepting Connections:
    - the server accepts a connection using accept()
    - this call blocks, until a client connects:
        -> returning a new socket object for the connection

c) Data exchange
    - use send() or sendall() to send data
    - use recv() to receive data

d) Close Sockets
    - properly close sockets with close() when done


### Client ###
a) Connect to Server:
    - the client connects to the server using connect((HOST, PORT))
        -> HOST: (the servers IP address) -> the ip address of host device!
        -> PORT: the port on which the server listens




