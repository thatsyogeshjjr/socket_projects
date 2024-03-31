import socket
# to implement threading


'''
TODO:
* handle POST methods with help of a form

'''

SERVER = 'localhost'
PORT = 5998

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

server.listen()
print(f'[+]\tserver is active on {SERVER}@{PORT}')


def render_page(req_type=None, http_param_data=None):
    '''
    POST request sends parameters in http request.
    We use http_param_data to handle such data

    Condition for parameters below checks if parameters exist
    inside the URL (will be the case for GET requests)
    '''
    file = req_data[1][1:]
    indata = None
    if req_type == 'POST':
        print(http_param_data)
        indata = {}
        for data_unit in params:
            data, val = data_unit.split('=')
            indata[data] = val

        print(f'[+]\t Altered params: {indata}')

    else:
        if '?' in file:
            file, params = file.split('?')[0], file.split('?')[
                1].split('&')
            print(f'[+]\tParameters:{params}')
            indata = {}
            for data_unit in params:
                data, val = data_unit.split('=')
                indata[data] = val

            print(f'[+]\t Altered params: {indata}')

    # valid if we plan to server only html pages
    if file[-5:] != '.html':
        file = file+'.html'

    file = open(file).read()

    if indata:
        for key, val in indata.items():
            file = file.replace('{{' + key + '}}', val)
            print('[!] REPLACED')

    client.send(b'HTTP/1.1 200 OK\r\n\r\n')
    for i in range(len(file)):
        client.send(file[i].encode())

    client.send(b'\r\n\r\n')


while True:
    client, addr = server.accept()
    print(f'[+]\t{addr} sent a request')

    req_data = client.recv(1024).decode()
    if not req_data:
        print('[-]\tMethod not allowed. Closing connection')
        client.sendall(b'HTTP/1.1 405 Method Not Allowed\r\n\r\n')
        client.close()
    req_data = req_data.split()

    match req_data[0]:
        case 'GET':
            print('[+]\tRequest type: GET')
            render_page()
            client.close()

        case 'POST':
            http_param_data = req_data[-1].split("&")
            print('[+]\tRequest type: POST')
            print(f'[!]\tRequest Data: {http_param_data}')
            render_page('POST', http_param_data)
            client.close()

    # client.close()
    # server.close()
    # break
