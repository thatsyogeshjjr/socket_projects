import socket
import threading
import datetime
import argparse
import time


'''
Arguments [for dev reference] 
-l --logs           : bool
-t --target         : string [IP address]
-f --flush          : expunge the log file
-sp --start-port    : starting port range
-tp --to-port       : ending port range

'''
parser = argparse.ArgumentParser(
    description='a simple network scanner project in python')
parser.add_argument('-l', '--logs', help='enable/disable logs', type=bool)
parser.add_argument(
    '-t', '--target', help='ip address of the scan target', type=str)
parser.add_argument('-f', '--flush', help='Purge the log file', type=bool)
parser.add_argument('-sp', '--start-port',
                    help='starting port range', type=int)
parser.add_argument('-tp', '--to-port', help='ending port range', type=int)
args = parser.parse_args()

startTime = time.time()
save_to_file = False if args.logs == None else args.logs
target = '192.168.29.131' if args.target == None else args.target
starting_port = 50 if args.start_port == None else args.start_port
ending_port = 5050 if args.to_port == None else args.to_port
t_IP = socket.gethostbyname(target)

print(f'Starting a scan on:\t{target}')


'''
system or well-known ports : 0 ~ 1023
user or registered ports   : 1024 ~ 49151
dynamic or private ports   : > 49152
'''

if args.flush:
    import os
    os.remove('logs.txt')
    print('[+]\tpurged logs.txt')


def handle_logs(operation, data=None):
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


if args.flush:
    handle_logs('flush')

if save_to_file:
    handle_logs('init')


def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn = s.connect_ex((t_IP, port))

    if conn == 0:
        print(f'{port}\t[OPEN]')
        if save_to_file:
            handle_logs('log', data=f'{port} [OPEN]\n')

    s.close()


for port in range(starting_port, ending_port):
    threading.Thread(target=scan_port, args=(port,)).start()
if save_to_file:
    handle_logs('end', data=f"Time taken\t{time.time() - startTime}\n")

print(f"Time taken\t{time.time() - startTime}")
