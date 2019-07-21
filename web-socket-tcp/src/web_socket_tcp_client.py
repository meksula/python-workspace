from socket import *

server_name = 'localhost'
server_port = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_name))
sentence = input('Some test statement...')
client_socket.send(sentence.encode())
modif_sentence = client_socket.recv(1024)
print('Received from server: ', modif_sentence.decode())
client_socket.close()
