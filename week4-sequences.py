#!/usr/bin/env python3

varString="Here is a nice string to splice"
varTuple = ("Here", "is", "a", "nice", "tuple", "to", "slice")
varList = ["Here", "is", "a", "nice", "list", "to", "splice" ]


print(f"{varString[3:]}")
print(f"{varString[:3]}")
print(f"{varString[3:11]}")
print(f"{varString[:24:2]} {varString[-4::2]}")
print(f"{varString[::-1]}")

print(f"{varList[::-1]}")
print(f"{varList[-5::-1]}")
print(f"{varList[::3]}")
print(f"{varList[1::]}")

for element in varString.split():
	print(element)

for element in varList:
	print(element)
