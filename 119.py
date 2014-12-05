#!/opt/swt/bin/python

def digitSum(n):
	r = 0
	if n > 9:
		while n:
			r, n = r + n % 10, n / 10
		return r
	else:
		return -1 # out of base/exponent range

bases = [[i] for i in range(2,100)] # the upper bound of this range is "cheating"
maxes = [bases[i][0] for i in range(0,len(bases))]
exponents = [1 for i in range(0,len(bases))]
sequence = []

while len(sequence) < 30:
	# print(maxes)
	baseIndex = maxes.index(min(maxes))
	# print(baseIndex)
	base = baseIndex + 2
	exponent = exponents[baseIndex] + 1
	# print(exponent)
	power = (base)**exponent
	bases[baseIndex].append(power)
	maxes[baseIndex] = power
	exponents[baseIndex] = exponent
	if digitSum(power) == base:
		print(base,exponent,power)
		sequence.append(power)
