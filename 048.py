import sys
# http://www.wolframalpha.com/input/?i=%28sum+i%5Ei%2C+i+from+1+to+1000%29+mod+10%5E10

numDigits = 10**10

def getLastTenOfProduct(i):
	product=1
	for power in range(1,i+1):
		product *= (i)
		product = product % numDigits
	return product

sum=0
for i in range(1,1001):
	sum += getLastTenOfProduct(i)
	sum = sum % numDigits
print sum % numDigits
