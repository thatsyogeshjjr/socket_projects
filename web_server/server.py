import socket


SERVER = 'localhost'
PORT = 5998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()

while True:

    client, addr = server.accept()
    try:
        #  file_name = client.recv(1024).decode(1024).split()[1]
        file_name = client.recv(1024).split()[1]

        f = open(file_name[1:])  # using [1:] to get rid of / in the URL
        output_data = f.read()

        # \r begins the print from the starting line

        client.send(b'HTTP/1.1 200 OK\r\n\r\n')
        for i in range(len(output_data)):
            client.send(output_data[i].encode())
        client.send(b'\r\n')
        client.close()

    except:
        client.send(b'HTTP/1.1 200 OK\r\n\r\n')
        client.send(b'<html><body><h1>404 not found</h1></body></html>')
        client.close()
