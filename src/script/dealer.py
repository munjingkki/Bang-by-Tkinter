import socket
import threading
def connect():
   s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = ''
   port=12222
   s.bind((host,port))

   s.listen(5)
   chat=None


   while True:
      if chat is None:
          # Halts
          print( '[Waiting for connection...]')
          chat, addr = s.accept() #  (socket object, address info) return
          print( 'Got connection from', addr)
      else:
          # Halts
          print( '[Waiting for response...]')
          print((chat.recv(1024)).decode('utf-8'))
threading.Thread(target=connect).start()
#when start, it run once.
class Dealer(object):
    import os
    deck=[i for i in os.listdir('../img') if i.startswith('g')]
    def shuffle(self):
        import random
        random.shuffle(self.deck)
        print(self.deck)
deck = Dealer()
deck.shuffle()
