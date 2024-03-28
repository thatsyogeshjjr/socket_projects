import socket
import threading

'''
Defined codes:
c101: Connection success. Send nickname

'''

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = 'CLIENT_DISCONNECT'
SERVER = socket.gethostname()

clients, nicknames = [], []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def broadcast(message: str):
    buff_length = len(message)
    for client in clients:
        client.send(str(buff_length).encode(FORMAT))
        client.send(message.encode(FORMAT))


def handle_clients(client: socket):
    while True:
        try:
            buff_length = client.recv(HEADER).decode(FORMAT)
            if buff_length:
                buff_length = int(buff_length)

                msg = client.recv(buff_length).decode(FORMAT)
                if msg == DISCONNECT_MSG:
                    raise Exception
                broadcast(msg)

        except:

            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat.')
            nicknames.remove(nickname)


def start_server():
    server.listen()
    while True:
        client, address = server.accept()
        client.send('c101'.encode(FORMAT))

        nickname = client.recv(1024).decode(FORMAT)
        nicknames.append(nickname)
        clients.append(client)
        print(f'{str(address)} is now connected!')
        broadcast(f'{nickname} joined the chat.')

        client_thread = threading.Thread(target=handle_clients, args=(client,))
        client_thread.start()


start_server()
