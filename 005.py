#!/opt/swt/bin/python
import sys

def isDivisibleByAll(number,factors):
	numFactors = len(factors)
	for i in range(0,numFactors):
		if number % factors[numFactors - 1 - i] != 0:
			return False
	print number
	return True


factors = range(1,20 + 1)
highestFactor = factors[len(factors) - 1]
startingPoint = 2520
while True:
	if isDivisibleByAll(startingPoint,factors):
		break
	startingPoint += highestFactor
