# Source - https://pymotw.com/2/socket/tcp.html

import socket
import sys

# Create TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('0.0.0.0', 25565) #TODO - change this later!
print("STARTING UP!")
sock.bind(server_address)

# Listen for connections
sock.listen(1) #TODO - what does 1 mean?

# Just chill until someone makes a connection
while True:
  connection, client_address = sock.accept()
  if connection:
    print("got a connection!")
    try:
      data = connection.recv(16)
      print("WE GOT DATA!", data)
      splitStrings = string.split(',')
      if len(splitStrings) == 0 and splitStrings[0] in printers and splitStrings[1] in (0,1):
        # WRITE TO THE FILE
        print("do something awesome here")
    finally:
      connection.close()