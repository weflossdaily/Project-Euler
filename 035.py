def isPrime(number,primes):
	for prime in primes:
		if number % prime == 0:
			# print str(number) + " is divisible by " + str(prime)
			return False
	primes.append(number)
	return True

def permuteNumString(numString):
	return numString[len(numString)-1] + numString[:-1]

def isCircularPrime(number,primes):
	numString = strNumber
	if isPrime(number,primes):
		newString = permuteNumString(numString)
		while newString != numString:
			if not isPrime(int(newString)):
				return False
			newString = permuteNumString(numString)
	else:
		return False
	return True


primes = []
count = 0
# get primes, since current function requires all earlier primes
for i in range(2,1000001):
	isPrime(i,primes)
print 'got primes'
for i in range(2,1000001):
	if isCircularPrime(i,primes):
		print i
		count += 1
print count
