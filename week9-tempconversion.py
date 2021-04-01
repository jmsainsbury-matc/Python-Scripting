#!/usr/bin/env python

import f2c
import c2f


temp = int(input("Please enter the temperature you wish to convert: "))
convertmode = input("Do you want to convert to fahrenheit[1] or celsius[2]: ")

if (convertmode == 1):
	c2f.main(temp)
elif (convertmode == 2):
	f2c.main(temp)

#f2c.main(temp)
#c2f.main(temp)
