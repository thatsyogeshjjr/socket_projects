import socket
import subprocess
import sys

SERVER = sys.argv[1]
PORT = int(sys.argv[2])


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER, PORT))

buff_size = int(s.recv(1024).decode())
cmd = s.recv(buff_size).decode()
print(f'To execute: {cmd}')
# subprocess.run(cmd.split())
