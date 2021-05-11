#!/usr/bin/env python3

import argparse, requests, bs4, json

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f', '--function-number', dest='FUNCTION_NUMBER', default=1, type=int, help='Select a function')
parser.add_argument('-ip', dest='IP_ADD', type=str, help='Enter an IP address')
SELECT_FUNCT = str(parser.parse_args().FUNCTION_NUMBER)
IP = parser.parse_args().IP_ADD
URL = "http://"+IP+"/q"+SELECT_FUNCT
if int(SELECT_FUNCT) < 5:
	print(SELECT_FUNCT)
	res = requests.get(URL)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
print("Name: Josh Sainsbury")
def get_response():
	print("Question 1 selected")
	print(URL)
	print(f"ANSWER: {soup}")
def parse_string():
	print("Question 2 selected")
	print(URL)
	h3 = str(soup.select('h3'))
	print(f"ANWSER: {h3[7:-6:3]}")
def parse_header():
	print("Question 3 selected")
	print(URL)
	headers = res.headers
	print(f"ANWSER: {headers['MATC-HEADER']}")
def parse_json():
	print("Question 4 selected")
	print(URL)
	json_raw = res
	json_dict = json.loads(json_raw.text)
	keynum = 0
	for keys in json_dict['Music And Books']:
		current_dict = json_dict['Music And Books'][keynum]
		if "author" in current_dict:
			if current_dict['title'] == '1984':
				print(f"ANSWER: {current_dict['author']}")
		keynum = keynum + 1
def q5():
	print("Question 5 selected")	
if SELECT_FUNCT == str(1):
	get_response()
elif SELECT_FUNCT == str(2):
	parse_string()
elif SELECT_FUNCT == str(3):
	parse_header()
elif SELECT_FUNCT == str(4):
	parse_json()
elif SELECT_FUNCT == str(5):
	q5()
else:
	print("Enter 1-5")
