import socket
import threading


class Proxy:
    def __init__(self) -> None:
        self.username = 'username'
        self.password = 'password'
        self.host = socket.gethostname()
        self.port = 14241

    def handle_client(self, connection):
        version, nmethods = connection.recv(2)
        methods = self.get_available_methods(nmethods, connection)
        if 2 not in set(methods):
            connection.close()
            return

        connection.sendall(bytes[SOCKS_VERSION, 2])

        if not self.verify_credentials(conn):
            return

    def verify_credentials(self, conn):
        pass

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen()

        while True:
            client, addr = s.accept()
            print(f"[+] New connection from {socket.gethostbyaddr(addr)}")
            threading.Thread(target=self.handle_client, args=(client,)).start()
