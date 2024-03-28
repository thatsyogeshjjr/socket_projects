import socket


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = 'CLIENT_DISCONNECT'
SERVER = socket.gethostname()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))


def send(message):
    message = message.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)

    # add padding to make the header fit in 64 bytes
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


print('''
=====================================
=          The Chatter              =
=====================================
      
write quit to exit
      
      ''')
while True:
    msg = input('Message: ')
    if msg == 'quit':
        send(DISCONNECT_MSG)
        break
    elif msg != '':
        send(msg)
