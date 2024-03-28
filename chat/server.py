import socket
import threading
import keyboard
import sys

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = 'CLIENT_DISCONNECT'
SERVER = socket.gethostname()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def handle_client(conn, addr):
    print(f'[+] {addr} is now connected.')
    connected = True

    while connected:

        # blocking line of code:
        # we won't move forward till smt is received.
        # Hence threading is used

        # How to know the length of msg
        # we use headers
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)

            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == 'CLIENT_DISCONNECT':
                connected = False
            print(f'{addr}:\t{msg}')


def kill_server(event):

    if event.name == 'esc':
        server.close()
        quit()
        sys.exit(0)


def start_server():
    server.listen()
    while True:

        keyboard.on_press(kill_server)

        (client, addr) = server.accept()
        threading.Thread(target=handle_client, args=(client, addr)).start()
        print(f'[!]\Active members: {threading.active_count()-1}')


start_server()
