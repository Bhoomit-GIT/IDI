import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a public host, and a port
    server_socket.bind(('localhost', 8080))

    # Become a server socket
    server_socket.listen(5)

    print("Server is listening on port 8080...")

    while True:
        # Accept connections from outside
        (client_socket, address) = server_socket.accept()
        print(f"Connection from {address} has been established.")

        # Receive the request
        request = client_socket.recv(1024).decode('utf-8')
        print(f"Received request: {request}")

        # Process the request (similar to HTTP method handling)
        if "GET_DATA" in request:
            response = "200 OK: Here is the data you requested."
        else:
            response = "400 BAD REQUEST: Unknown command."

        # Send a response
        client_socket.send(response.encode('utf-8'))

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
