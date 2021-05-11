#!/usr/bin/env python3

import argparse, requests, bs4, json, socket

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f', '--function-number', dest='FUNCTION_NUMBER', default=1, type=int, help='Select a function')
parser.add_argument('-ip', dest='IP_ADD', type=str, help='Enter an IP address')
SELECT_FUNCT = str(parser.parse_args().FUNCTION_NUMBER)
IP = parser.parse_args().IP_ADD
URL = "http://"+IP+"/q"+SELECT_FUNCT
if int(SELECT_FUNCT) < 5:
	res = requests.get(URL)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
if int(SELECT_FUNCT) == 5:
	RHOST = IP
	RPORTS = range(5000,6000)
	SND_DATA = 'secret'
print("Name: Josh Sainsbury")
print(URL)
def get_response():
	#print("Question 1 selected")
	print(f"ANSWER: {soup}")
def parse_string():
	#print("Question 2 selected")
	h3 = str(soup.select('h3'))
	print(f"ANWSER: {h3[7:-6:3]}")
def parse_header():
	#print("Question 3 selected")
	headers = res.headers
	print(f"ANWSER: {headers['MATC-HEADER']}")
def parse_json():
	#print("Question 4 selected")
	json_raw = res
	json_dict = json.loads(json_raw.text)
	keynum = 0
	for keys in json_dict['Music And Books']:
		current_dict = json_dict['Music And Books'][keynum]
		if "author" in current_dict:
			if current_dict['title'] == '1984':
				print(f"ANSWER: {current_dict['author']}")
		keynum = keynum + 1
def socket_client():
	#print("Question 5 selected")
	for RPORT in RPORTS:
		C_SOCK = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		C_SOCK.settimeout(2)
		try:
			C_SOCK.connect((RHOST,RPORT))
			C_SOCK.send(bytearray(SND_DATA,'utf8'))
			RCV_DATA = C_SOCK.recv(1024)
			print(f"ANWSER: {RCV_DATA.decode('utf-8')}")
			C_SOCK.close()
		except socket.error as e:
			C_SOCK.close()
if SELECT_FUNCT == str(1):
	get_response()
elif SELECT_FUNCT == str(2):
	parse_string()
elif SELECT_FUNCT == str(3):
	parse_header()
elif SELECT_FUNCT == str(4):
	parse_json()
elif SELECT_FUNCT == str(5):
	socket_client()
else:
	print("Enter 1-5")
