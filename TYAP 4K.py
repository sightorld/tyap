import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
s.connect((host, port))
s.send(input().encode())   
data = s.recv(1000000).decode()
print (data)
s.close()
