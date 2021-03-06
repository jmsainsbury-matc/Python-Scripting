#!/usr/bin/env python3

import socket

LHOST = ''
LPORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((LHOST, LPORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			print(data)
			if not data:
				break
			conn.sendall(data)
