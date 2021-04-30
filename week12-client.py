#!/usr/bin/env python3

import socket

RHOST = '127.0.0.1'
RPORT = 5000
SND_DATA = 'HELLO'

C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	C_SOCK.connect((RHOST, RPORT))
	while True:
		SND_DATA = input("Enter your message: ")
		C_SOCK.send(bytearray(SND_DATA,'utf8'))
		RCV_DATA = C_SOCK.recv(1024)
		print(RCV_DATA)

except socket.error as e:
	print(f"Connection State: {RPORT}::{e}")
	C_SOCK.close()
