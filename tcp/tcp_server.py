from socket import AF_INET, SOCK_STREAM, socket

PORT = 12000

with socket(AF_INET, SOCK_STREAM) as server_socket:
    server_socket.bind(('', PORT))
    server_socket.listen(1)
    print('Server is ready to receive')
    while True:
        connection_socket, address = server_socket.accept()
        message = connection_socket.recv(2048).decode()
        result = message.upper()
        connection_socket.send(result.encode())
        connection_socket.close()
