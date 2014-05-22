import sys

numDigits = 10**10

def getLastTenOfProduct(base, exponent):
	product=1
	for power in range(1,exponent+1):
		product *= (base)
		product = product % numDigits
	return product

sum = getLastTenOfProduct(2,7830457)
sum *= 28433
sum += 1
print sum % numDigits
