def isPalindromic(numberString):
	length = len(numberString)
	halfway = length/2
	i = 0
	while i <= halfway:
		if numberString[i] != numberString[length - i]:
			return False
	return True

def getHighestPowerOf2(number):
	exponent = 0
	product = 2**exponent
	while True:
		if number == product:
			return exponent
		elif product > number:
			return (exponent - 1)
		else:
			exponent += 1
			product *= 2

def convertBase10To2(number):
	conversion = ''
	for exponent in reversed(range(getHighestPowerOf2(number)+1)):
		exponentiation = 2**exponent
		if number >= exponentiation:
			conversion += '1'
			number -= exponentiation
			exponentiation /= 2
		else:
			conversion += '0'
	return conversion

total = 0
i = 0
while i < 1000000:
	i+=1
	if isPalindromic(str(i)) and isPalindromic(convertBase10To2(i)):
		print str(i) + ', ' + convertBase10To2(i)
		total += i
print total
