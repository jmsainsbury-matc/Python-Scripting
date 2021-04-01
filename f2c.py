#!/usr/bin/env python3

def f2c(degrees_fahrenheit):
	degrees_celsius = (degrees_fahrenheit - 32) * 5/9
	return degrees_celsius

def main():
	temp = int(input("Enter the degrees in fahrenheit: "))
	print(f2c(temp))

if __name__ == "__main__":
	main()
