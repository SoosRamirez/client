import socket
import threading


def read_sock():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


server = 'localhost', 48395
alias = input("print Nickname:")
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))
sor.sendto((alias + ' Connect to server').encode('utf-8'), server)
potok = threading.Thread(target=read_sock)
potok.start()
while True:
    message = input()
    sor.sendto(('[' + alias + ']' + message).encode('utf-8'), server)
