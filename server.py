from http import client
import socket
import threading
from tkinter import messagebox
# from socket import *
# from threading import *
from torch import true_divide 
from tkinter import *
#192.168.1.119
# HOST = "127.0.0.1" #loopback
SERVER_PORT = 65432 
FORMAT = "utf-8"
SERVER = socket.gethostbyname(socket.gethostname())


def clientThread(clientSocket, clientAddress):
    connected = True
    while connected:
        # try:
        #     data = clientSocket.recv(1024).decode(FORMAT)
        #     clientSocket.send(data).encode(FORMAT)
        #     # else:
        #     #     raise error('Client disconnected')
        # except:
        #     print('Client disconnected')
        #     connected = False
        #     clientSocket.close()
        data = clientSocket.recv(1024).decode(FORMAT)
        clientSocket.sendto(data.encode(FORMAT), (SERVER, SERVER_PORT) )
    clientSocket.close()
        



# Khai báo socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Trên sever sẽ có 1 socket đang lắng nghe
s.bind((SERVER, SERVER_PORT))

def start():
    s.listen()
    print(f"Server is listening on {SERVER}")
    while True:
        clientSocket, clientAddress = s.accept()
        print("SERVER SIDE")
        print("server:", SERVER, SERVER_PORT)
        print("Waiting for Client...")
        # messagebox.showinfo("Server", "Waiting for Client...")
        print(f"Connected to {clientAddress}")
        thread = threading.Thread(target=clientThread, args=(clientSocket, clientAddress))
        thread.daemon = True 
        thread.start()
        # root.mainloop()
start()
