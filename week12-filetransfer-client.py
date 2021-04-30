#!/usr/bin/env python3
import socket

RHOST = '127.0.0.1'
RPORT = 5050



C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
C_SOCK.connect((RHOST, RPORT))

with open("filetosend","r") as hfile:
	data = hfile.readline()
	while data:
		C_SOCK.send(bytearray(data,'utf8'))
		data = hfile.readline()



print(data)
