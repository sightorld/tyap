import socket
import sys
from time import localtime, strftime
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 8007
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024).decode()
if data == 'date time':
    data = strftime("%d.%m.%Y %H:%M:%S", localtime())
else:
    data = 'unknown command'
print ('Sent "'+data+'" to', addr[0]+':'+str(addr[1]))
conn.send(data.encode())
conn.close()
