# http://mathworld.wolfram.com/MultiplicativeOrder.html
# wish i could take credit

def isRelativelyPrime(a,b):
	# TODO: make a prime module and put a better version of this there
	small = 0
	big = 0
	if a < b:
		small = a
		big = b
	else:
		small = b
		big = a
	for i in range(2,small + 1):
		if small % i == 0 and big % i == 0:
			return False
	return True

currentBestDenominator = 3
currentBestDenominatorPeriod = 1

for d in range(4,1001):
	if isRelativelyPrime(10,d):
		e = 1
		while pow(10,e) % d != 1:
			e += 1
		if e > currentBestDenominatorPeriod:
			currentBestDenominatorPeriod = e
			currentBestDenominator = d

print(currentBestDenominator)