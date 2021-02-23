#!/usr/bin/env python3


with open("/etc/passwd","r") as hFile:
	strPasswd=hFile.read()
	print(len(strPasswd))
	print("The lenght function counts how many characters are in the string")
	print("The length function could be used to count how long a users password is")
with open("/etc/passwd","r") as hFile:
	listPasswd=hFile.readlines()
	print(len(listPasswd))
	print("When used with a list the lenght funcitons prints the number of elements")
	

