from socket import *

server_name = 'localhost'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
message = input('Input sentence')
client_socket.sendto(message.encode(), (server_name, server_port))
modif_msg, server_addr = client_socket.recvfrom(2048)
print(modif_msg.decode())
client_socket.close()
