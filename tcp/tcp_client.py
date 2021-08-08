from socket import AF_INET, SOCK_STREAM, socket


SERVER = '127.0.0.1'
SERVER_PORT = 12000

message = input('Input lowercase sentence: ')
with socket(AF_INET, SOCK_STREAM) as client_socket:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((SERVER, SERVER_PORT))
    client_socket.send(message.encode())
    result = client_socket.recv(1024)
    print(f'From server: {result.decode()}')
