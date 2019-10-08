import socket

HOST='127.0.0.1'  #Standard loopback interface address (localhost)
POST=9999  # Port to listen on

with scocket.socket(socket.AF_INET, socket.SOCK_STREQAM) as s:
   s.connect((HOST,PORT))
   s.sendall(b'Hello,Server')
   data=s.recv(1024)
   print ('Received', repr(data))
