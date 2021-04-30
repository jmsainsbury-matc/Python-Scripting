#!/usr/bin/env python3
import socket

LHOST = ''
LPORT = 5050
hfile = open("filetoreceive","w")
hfile.truncate(0)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((LHOST, LPORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			data = data.decode("utf-8")
			print(data)
			hfile.write(data)
			if not data:
				 break
hfile.close()
