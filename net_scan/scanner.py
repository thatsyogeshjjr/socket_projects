import socket
import threading
import time

'''
system or well-known ports : 0 ~ 1023
user or registered ports   : 1024 ~ 49151
dynamic or private ports   : > 49152
'''


startTime = time.time()

target = '192.168.29.131'
t_IP = socket.gethostbyname(target)
print(f'Starting a scan on:\t{target}')


def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex((t_IP, port))

    if conn == 0:
        print(f'[OPEN] {port}')
    s.close()


for port in range(50, 500):
    threading.Thread(target=scan_port, args=(port,)).start()
print(f"Time taken:\t{time.time() - startTime}")
