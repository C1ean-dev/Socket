import socket
import threading
import time

host = '127.0.0.1'
port = 50000
nickname = input("escolha seu nickname: ")


try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
except Exception as inst:
    print(inst)


def receive_connection_to_server():
    run = True
    while run:
        try:
            # request for echo connection from server
            message = client.recv(1024).decode('utf-8')
            if message == 'OK':
                # send nickname from server
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except Exception as inst:
            # Close Connection
            print(inst)
            client.close()
            break


def send_message_to_server():
    run = True
    while run:
        time.sleep(1)
        print(f'{nickname} digite a mensagem>>>')
        message = f'{nickname}: {input()}'
        client.send(message.encode('utf-8'))


# Starting Threads
receive_thread = threading.Thread(target=receive_connection_to_server)
receive_thread.start()

write_thread = threading.Thread(target=send_message_to_server)
write_thread.start()
