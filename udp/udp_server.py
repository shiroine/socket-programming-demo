from socket import AF_INET, SOCK_DGRAM, socket

PORT = 12000
BUFFER = 2048

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', PORT))
print('Server started to receive')
is_close = False
while not is_close:
    message_bytes, client_address = server_socket.recvfrom(BUFFER)
    result = message_bytes.decode().upper()
    if result == 'CLOSE':
        is_close = True
        result = 'Bye'
    server_socket.sendto(result.encode(), client_address)
