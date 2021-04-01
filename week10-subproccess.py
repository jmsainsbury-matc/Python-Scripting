#!/usr/bin/env python3
import subprocess

#print(type(subprocess.run(['ps', '-axco', 'command'])))
myProc = subprocess.run(['ps', '-axco', 'command'],stdout=subprocess.PIPE)
myProcString = myProc.stdout.decode()
myProcList = myProc.stdout.decode().split('\n')
print(len(myProcList))
for lines in myProcList:
	print(lines)
