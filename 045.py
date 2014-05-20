#!/opt/swt/bin/python
import sys
import math

def isTriangular(n):
	return (math.sqrt((8 * n) + 1) - 1) % 2 == 0

def isPentagonal(n):
	return (math.sqrt((24 * n) + 1) + 1) % 6 == 0

def getHexagonal(n):
	return n * (2 * n - 1)

def findNextHexaPentaTriangle(i):
	while(True):
		i+=1
		hexagon = getHexagonal(i)
		if isPentagonal(hexagon):
			if isTriangular(hexagon):
				print str(hexagon)
				return

findNextHexaPentaTriangle(143)
