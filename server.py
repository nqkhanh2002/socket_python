from http import client
import socket
from socket import *
from threading import *

from torch import true_divide 
def clientThread(clientSocket, clientAddress):
    while True:
        try:
            data = clientSocket.recv(1024).decode(FORMAT)
            if data:
                clientSocket.send(data).encode(FORMAT)
            else:
                raise error('Client disconnected')
        except:
            clientSocket.close()
            return False

#192.168.1.119
HOST = "127.0.0.1" #loopback
SERVER_PORT = 65432 
FORMAT = "utf8"
# Khai báo socket
s = socket(AF_INET, SOCK_STREAM) 
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Trên sever sẽ có 1 socket đang lắng nghe
s.bind((HOST, SERVER_PORT))
s.listen()

print("SERVER SIDE")
print("server:", HOST, SERVER_PORT)
print("Waiting for Client...")

while True:
    clientSocket, clientAddress = s.accept()
    print("client address:",clientAddress)
    thread = Thread(target=clientThread, args=(clientSocket, clientAddress))
    thread.start()
    