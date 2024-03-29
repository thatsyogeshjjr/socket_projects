import socket
# to implement threading


SERVER = 'localhost'
PORT = 5998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()
print(f'[+]\tserver is active on {SERVER}@{PORT}')

while True:
    client, addr = server.accept()
    print(f'[+]\t{addr} sent a request')

    req_data = client.recv(1024).decode()
    print(req_data)
    if not req_data:
        print('[-]\tMethod not allowed. Closing connection')
        client.sendall(b'HTTP/1.1 405 Method Not Allowed\r\n\r\n')
        client.close()
    req_data = req_data.split()

    match req_data[0]:
        case 'GET':
            print('[+]\tRequest type: GET')
            file = req_data[1][1:]
            if '?' in file:
                file, params = file.split('?')[0], file.split('?')[
                    1].split('&')
                print(f'[+]\tParameters:{params}')
            file = open(file).read()
            client.send(b'HTTP/1.1 200 OK\r\n\r\n')
            for i in range(len(file)):
                client.send(file[i].encode())
            client.send(b'\r\n\r\n')

        case 'POST':
            print('[+]\tRequest type: POST')
            print()
            pass

    client.close()
    server.close()
    break
