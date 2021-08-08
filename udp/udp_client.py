from socket import AF_INET, SOCK_DGRAM, socket

SERVER = '127.0.0.1'
SERVER_PORT = 12000
BUFFER = 2048

message = input('Input lowercase sentence: ')
with socket(AF_INET, SOCK_DGRAM) as client_socket:
    client_socket.sendto(message.encode(), (SERVER, SERVER_PORT))
    modified_message, server_address = client_socket.recvfrom(BUFFER)
    print(modified_message.decode())
