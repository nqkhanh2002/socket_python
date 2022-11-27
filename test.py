import socket
import threading

s = socket.gethostbyname(socket.gethostname())
print(s)