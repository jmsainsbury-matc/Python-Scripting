#!/usr/bin/env python3

print("Name:Josh Sainsbury")
Total = 0
with open("Midterm-if.txt","r") as hFile:
	line = hFile.readline()
	while line:
		linesplit = line.split(',')
		for element in linesplit:
			element = element.strip()
			if element.isnumeric():
				linenum = int(element)
			if (element == "gmeach18@ed.gov") or (element == "248.253.63.149") or (element == "Whiteland") or (element == "80.222.19.190") \
				or (element == "Kayley") or (element == "dcassyqw@microsoft.com"):
				print(element)
				Total += linenum
		line = hFile.readline()
print(Total)
