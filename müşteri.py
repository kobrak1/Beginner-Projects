import socket
import time

SERVER="192.168.56.1"
PORT=8080
ADDR=(SERVER, PORT)

s=socket.socket()
s.connect(ADDR)
time.sleep(1)

print('connected to server..')

msg=input('Message:')
s.send(bytes(msg,'utf-8'))
