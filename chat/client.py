import socket
import threading


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = 'CLIENT_DISCONNECT'
SERVER = socket.gethostname()

nickname = input('Nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def handle_recv():
    while True:
        buffer = client.recv(HEADER).decode(FORMAT)
        print(f"[FOR DEV] buffer_values: {buffer}")
        if buffer:
            if buffer == 'c101':
                client.send(nickname.encode(FORMAT))
            else:
                len_msg = int(buffer)
                msg = client.recv(len_msg).decode(FORMAT)
                print(msg)


def writer():
    while True:
        message = f"{nickname}: {input('Message: ')}"
        client.send(str(len(message)).encode(FORMAT))
        client.send(message.encode(FORMAT))


threading.Thread(target=handle_recv).start()
threading.Thread(target=writer).start()
