#!/opt/swt/bin/python
import sys
import math

def isPrime(number,primes):
	for prime in primes:
		if number % prime == 0:
			# print str(number) + " is divisible by " + str(prime)
			return False
	primes.append(number)
	return True

def isFactorOf(potentialFactor,number):
	quotient = number
	remainder = 0
	while remainder == 0:
		remainder = quotient % potentialFactor
		if remainder == 0:
			# print str(quotient) + " is divisible by " + str(potentialFactor)
			quotient /= potentialFactor
	return quotient

# input
number = 600851475143

# keep an arsenal of primes as you find them
primes = []

# let's try some factors
currentPotentialFactor = 2
while currentPotentialFactor <= number:
	if isPrime(currentPotentialFactor,primes):
		number = isFactorOf(currentPotentialFactor,number)
	currentPotentialFactor += 1
print primes[len(primes) - 1]
