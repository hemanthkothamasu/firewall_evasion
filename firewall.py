
import socket
import json
import time
#creating the socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
print host

port = 2002
s.connect(('127.0.0.1',port))
s.sendall('{"command":"A')
time.sleep(5)
s.sendall('U')
time.sleep(4)
s.sendall('T')
time.sleep(3)
s.sendall('H","user": "relaxedcommander"}')

#receiving the Data
r=s.recv(1024)
#printing result
print "Result", result
s.close
