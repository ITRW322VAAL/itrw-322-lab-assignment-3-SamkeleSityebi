import socket

HOST='127.0.0.1'  #Standard loopback interface address (localhost)
POST=9999  # Port to listen on

with scocket.socket(socket.AF_INET, socket.SOCK_STREQAM) as s:
   s.bint((HOST,PORT))
   s.listen()
   conn, addr= s.accept()
   with conn:
     print('Server is connected with address',  addr)
	 while True:
	  data=conn.recv(2048) #default byte stream size
	    if not data:
		  break
		conn.sendall(data)
