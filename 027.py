import sets
currentPrimes = Set.([1])

max = 0
bestA = 0
bestB = 0
for a in range(-999,1000):
	for b in range(-999,1000):
		
		numPrimes = countConsecutivePrimes(a,b,currentPrimes)
		if numPrimes > max:
			max = numPrimes
			bestA = a
			bestB = b
print a*b