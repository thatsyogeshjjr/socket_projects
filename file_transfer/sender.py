import socket
import os

SERVER = socket.gethostname()
PORT = 5959

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.bind((client, PORT))
client.connect((SERVER, PORT))

file = open('./image.jpg', 'rb')
file_size = os.path.getsize('image.jpg')


client.send('received_image.png'.encode())
client.send(str(file_size).encode())

data = file.read()
client.sendall(data)

client.send(b'<END OF FILE>')

file.close()
client.listen()
