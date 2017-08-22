
from board_UI import *
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.56.101'
port=12222

s.connect((host,port))
print('Connected to ',host)

def chat():
    global s
    while True:
        chat=input("chat : ")
        s.send(chat.encode('utf-8'))
def recv():
    global s
    while True:
        a=s.recv(1024)
        if a:
            print ((a).decode('utf-8'))

threading.Thread(target=chat).start()
threading.Thread(target=recv).start()

root.mainloop()