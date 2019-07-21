from socket import *

server_port = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', server_port))
print("Server script is ready for UDP request handling")

while True:
    message, client_addr = server_socket.recvfrom(2048)
    modif_msg = message.decode().upper()
    server_socket.sendto(modif_msg.encode(), client_addr)