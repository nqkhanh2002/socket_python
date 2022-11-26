import socket
import threading

PORT = 5050
s = socket.gethostbyname(socket.gethostname())
print(s)