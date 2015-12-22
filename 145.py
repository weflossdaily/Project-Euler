def isReversible(num):
	numString = str(num)

	if numString.endswith('0'):
		return False

	for digit in str(num + int(numString[::-1])):
		if int(digit) % 2 == 0:
			return False
	return True

numReversible = 0
for i in range(1000000000):
	if isReversible(i):
		numReversible += 1
print(numReversible)