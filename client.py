import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(('localhost', 8080))

    # Send a request (similar to an HTTP GET method)
    client_socket.send("GET_DATA".encode('utf-8'))

    # Receive the response
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Received response: {response}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
