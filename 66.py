#!/usr/bin/env python
#  Bruteforce all possible values of x where x^2 - d * y^2 = 1 to find the maximum value of x
#  I realize this is not the best possible solution xD


def findxmax(x,d,y,xmax):
	ans = x**2 - d * y**2
	if ans == 1:
		xmax = x if x > xmax else xmax
		x = 1
		d = d - 1
		y = 1
		findxmax(x, d, y, xmax)
	elif ans > 1:
		y -= 1
		findxmax(x, d, y, xmax)
	elif ans < 1:
		x = x - 1
		y = 1
		findxmax(x, d, y, xmax)
	elif d == 0:
		return xmax		
	
if __name__ == "__main__":
	print "xmax : {}".format(findxmax(x = 2, d = 1000, y = 1, xmax = 0))
	
