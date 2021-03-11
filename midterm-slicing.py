#!/usr/bin/env python3
print("Name: Josh Sainsbury")

with open("slicing-file.txt","r") as hfile:
	file = hfile.read().strip().split('\n')
	va = file[-3]
	vb = file[2:5]
	vc = file[-10:12:-2]
	vd = file[10:13]
	ve = file[-19:-22:-1]
seperator = ' '
quote = va + " " + seperator.join(vb) + " " + seperator.join(vc) + " " + seperator.join(vd) + " " + seperator.join(ve)
print(quote)
