import socket
SERVER = '127.0.0.1'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER, PORT))
s.listen()

client, addr = s.accept()
print(f'[+] Connection from {client}')
while True:
    cmd = input('Command> ')
    client.send(str(len(cmd)).encode())
    client.send(cmd.encode())

    output_buf = client.recv(1024)
    print(f'OUTPUT BUFFER:::  {output_buf}')
    print(f'DECODED::: {output_buf.decode()}')
    output = client.recv(int(output_buf)).decode()
    print()
    print(output)
