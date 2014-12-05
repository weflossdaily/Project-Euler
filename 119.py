#!/opt/swt/bin/python

def digitSum(n):
	r = 0
	while n:
		r, n = r + n % 10, n / 10
	return r

maxPowers = [i for i in range(2,100)] # the upper bound of this range is "cheating." The lower the value, the faster this performs, but I have put no thought into why we only need this many.
exponents = [1 for i in range(0,len(maxPowers))]
sequence = []

# we also stop prematurely; sequence should be an ordered set and we should continue until every element of maxPowers is greater than the 30th smallest element in sequence
while len(sequence) < 30:
	baseIndex = maxPowers.index(min(maxPowers))
	base = baseIndex + 2
	exponent = exponents[baseIndex] + 1
	power = (base)**exponent
	maxPowers[baseIndex] = power
	exponents[baseIndex] = exponent
	if digitSum(power) == base:
		print(base,exponent,power)
		sequence.append(power)
