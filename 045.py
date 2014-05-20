#!/opt/swt/bin/python
import sys
import math

# def isEven(n):
# 	return n % 2 == 0

# def isDivisibleByThree(n):
# 	return n % 3 == 0

def isTriangular(n):
	# twoN = 2 * n
	# squareRoot = math.sqrt(twoN)
	# low = math.floor(squareRoot)
	# if low * low + low == twoN:
	# 	print str(n) + ' is triangular!'
	return (math.sqrt((8 * n) + 1) - 1) % 2 == 0

def isPentagonal(n):
	return (math.sqrt((24 * n) + 1) + 1) % 6 == 0

def getHexagonal(n):
	return n * (2 * n - 1)


i = 143
while(True):
	i+=1
	hexagon = getHexagonal(i)
	if isPentagonal(hexagon):
		if isTriangular(hexagon):
			print str(hexagon) + ' yay!'
