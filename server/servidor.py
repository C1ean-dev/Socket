import socket
import threading

# variaveis globais
#
host = 'localhost'
port = 50000  # porta mae do servidor adicionar portas para criar grupos a partir dessa
address = (host, port)

# lista de clients e nicknames
#
client_list = []
nickname_list = []

# inicia um server ipv4, tcpip e tenta atribuir uma porta à servidor e "escuta" os clintes que tentarm conectar
# iniciando servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('server initial')

server.bind(address)
print(host, port)

server.listen()
print('waiting connection')


# send message to all online clients on the server
#
def enviar_menssagem(mensagem):
    for client in client_list:
        client.send(mensagem)


def tratar_client(client):
    run = True
    while run:
        try:
            # receive messages from the client
            message = client.recv(1024)
            enviar_menssagem(message)
        except Exception as e:
            # remove disconnected client
            print(e)
            index = client_list.index(client)
            client_list.remove(client)
            client.close()
            nickname = nickname_list[index]
            enviar_menssagem(f'{nickname} left!'.encode('utf-8'))
            nickname_list.remove(nickname)
            break


def receive_and_listener():
    run = True
    while run:
        # Accept Connection
        client, address = server.accept()
        print(f"Connected with {str((host, port))}")

        # Request And Store Nickname
        client.send('OK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nickname_list.append(nickname)
        client_list.append(client)

        # Print nicknames for all clients server
        print(f'nick name is {nickname}')
        enviar_menssagem(f'Your Nickname is {nickname}'.encode('utf-8'))
        enviar_menssagem(f'{nickname} joined!\n'.encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        # Start Thread For Client
        thread = threading.Thread(target=tratar_client, args=(client,))
        thread.start()


receive_and_listener()
