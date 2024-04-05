import socket
import threading
import datetime
import time

'''
system or well-known ports : 0 ~ 1023
user or registered ports   : 1024 ~ 49151
dynamic or private ports   : > 49152
'''


def handle_logs(operation, data=None, ):
    with open('logs.txt', 'a') as logfile:
        match operation:
            case 'init':
                logfile.write(
                    f'Operation Started: {datetime.datetime.now()}\n')
            case 'log':
                logfile.write(data)
            case 'end':
                logfile.write(f'Operation Ended: {datetime.datetime.now()}\n')
                logfile.write(data)
            case 'flush':
                import subprocess
                subprocess.run('rm logs.txt'.split())


startTime = time.time()
save_to_file = True

if save_to_file:
    handle_logs('init')

target = '192.168.29.131'
t_IP = socket.gethostbyname(target)
print(f'Starting a scan on:\t{target}')


def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex((t_IP, port))

    if conn == 0:
        print(f'{port}\t[OPEN]')
        if save_to_file:
            handle_logs('log', data=f'{port} [OPEN]\n')

    s.close()


for port in range(50, 500):
    threading.Thread(target=scan_port, args=(port,)).start()
if save_to_file:
    handle_logs('end', data=f"Time taken\t{time.time() - startTime}\n")

print(f"Time taken\t{time.time() - startTime}")
