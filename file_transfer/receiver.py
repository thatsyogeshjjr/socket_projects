import socket


SERVER = socket.gethostname()
PORT = 5959


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))
server.listen()
client, addr = server.accept()

file_name = client.recv(1024).decode()
file_size = client.recv(1024).decode()

file = open(file_name, 'wb')
file_bytes = b""
done = False

while not done:
    data = client.recv(1024)
    if file_bytes[-13:] == b'<END OF FILE>':
        done = True
    else:
        file_bytes += data
        print('wait....')


file.write(file_bytes)
server.close()
client.close()
