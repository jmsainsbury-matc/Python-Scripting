#!/usr/bin/env python3

def c2f(degrees_celsius):
	degrees_fahrenheit = (degrees_celsius * 9/5) + 32
	return degrees_fahrenheit

def main():
	temp = int(input("Enter the degrees in celsius: "))
	print(c2f(temp))

if __name__ == "__main__":
	main()
