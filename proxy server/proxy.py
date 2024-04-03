import socket
import sys
import threading

PORT = 4444
SERVER = '127.0.0.1'

buffer_size = 8192


def proxy_server(webserver, port, client, data, addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, client))
        s.send(data)

        while True:
            reply = s.recv(buffer_size)

            if len(reply) > 0:
                client.send(reply)
                data = float(len(reply))
                dar = "{}.3s".format(dar)
                print(f"[*] Request Done: {addr[0]} => {dar} <= {webserver}")
            else:
                break

            s.close()
            client.close()

    except socket.error:
        s.close()
        client.close()
        sys.exit(1)


def handle_client(client, data, addr):
    try:
        print(data)
        first_line = data.split("\n")[0]
        url = first_line.split(" ")[1]

        http_pos = url.find('://')
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]

        port_pos = temp.find(":")
        webserver_pos = temp.find('/')

        if webserver_pos == -1:
            webserver_pos = len(temp)

        webserver = 0
        port = -1

        if port_pos == -1 or webserver_pos < port_pos:
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int(temp[(port_pos+1):][:webserver_pos - port_pos - 1])
            webserver = temp[:port_pos]

        # print(webserver)
        proxy_server(webserver, port, client, data, addr)
    except Exception as e:
        print(e)


def main():
    max_conn = 5

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER, PORT))
    s.listen(max_conn)

    while True:
        try:
            print('[++]hello0')
            client, addr = s.accept()
            data = client.recv(buffer_size)
            print('[++]hello1')
            print(data)
            threading.Thread(target=handle_client(client, data, addr)).start()

        except KeyboardInterrupt:
            s.close()
            sys.exit(1)
            break

        except Exception as e:
            print(e)
            sys.exit(2)

    s.close()


if __name__ == "__main__":
    main()
