import socket

host = '127.0.0.1'
port = 50000

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
except Exception as inst:
    print(inst)

#envia o nome do arquivo para o servidor
#
name_file = str(input('digite o nome do arquivo>>>'))
client.send(name_file.encode())

# le e monta o arquivo
#
try:
    with open(name_file, 'wb') as file:
        while True:
            data = client.recv(1000000)
            if not data:
                break
            file.write(data)
    print(f'{name_file} recebido')
except Exception as inst:
    print(inst)
client.close()

