#!/usr/bin/env python3

import argparse, requests, json
parser = argparse.ArgumentParser(description="Enter an IP address to get information about it")


parser.add_argument('-ip', '--ip-address', dest='varIP', type=str, required=True, help='Enter the ip address') 

varIP=(parser.parse_args()).varIP
varIP= "https://ipinfo.io/"+ varIP +"/json"

print(varIP)
json_raw = requests.get(varIP)
myDict = json.loads(json_raw.text)


for key in myDict: 
	print(f"{key} : {myDict[key]}")
