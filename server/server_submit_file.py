import socket

# variaveis globais
#
host = 'localhost'
port = 50000
address = (host, port)

# inicia um server ipv4, tcpip e tenta atribuir uma porta à servidor e "escuta" os clintes que tentarm conectar
# iniciando servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('server initial')

server.bind(address)

server.listen()
print('waiting connection')

connection, address = server.accept()

name_file = connection.recv(1024).decode()
try:
    with open(name_file, 'rb') as file:
        for data in file.readlines():
            connection.send(data)
except Exception as e :
    print("An exception occurred", e)
