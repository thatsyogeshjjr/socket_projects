import socket
import threading


SERVER = 'localhost'
PORT = 5998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()


def handle_client(client):
    try:
        #  file_name = client.recv(1024).decode(1024).split()[1]

        '''
        FOR REFERENCE: the web browswer sends this to the server
        b'GET /site.html HTTP/1.1\r\nHost: localhost:5998\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate, br\r\nDNT: 1\r\nConnection: keep-alive\r\nCookie: csrftoken=f7wb8cvgUdIPTpERkBVYpv4WEQ4IqNSj; tabstyle=html-tab\r\nUpgrade-Insecure-Requests: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\n\r\n'
        '''

        file_name = client.recv(1024).split()[1]

        f = open(file_name[1:])  # using [1:] to get rid of / in the URL
        output_data = f.read()

        # \r begins the print from the starting line

        client.send(b'HTTP/1.1 200 OK\r\n\r\n')
        for i in range(len(output_data)):
            client.send(output_data[i].encode())
        client.send(b'\r\n')
        # client.close()

    except:
        client.send(b'HTTP/1.1 200 OK\r\n\r\n')
        client.send(b'<html><body><h1>404 not found</h1></body></html>')
        client.close()


while True:

    client, addr = server.accept()
    print(f'\rClients connected: {str(threading.activeCount())}\r')
    threading.Thread(target=handle_client, args=(client,)).start()
