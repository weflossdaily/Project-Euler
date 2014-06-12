import math

def dOfN(n):
	sum = 0
	i = 0
	bound = n/2
	while i < bound:
		i+=1
		if (n % i) == 0:
			sum += i
	return sum

sum = 0
for i in range(1,10000):
	b = dOfN(i)
	a = dOfN(b)
	if a==i and i!=b:
		#print str(i) + ', ' + str(b) + ', ' + str(a)
		sum += i
print sum