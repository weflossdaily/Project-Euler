def sumFactors(number):
	potentialFactor = 1
	factorSum = 0
	upperLimit = number/2
	while potentialFactor < upperLimit:
		if number % potentialFactor == 0:
			factorSum += potentialFactor
		potentialFactor += 1
	return factorSum

def isAbundant(number,abundantInventory,nonAbundantInventory):
	if number in abundantInventory:
		return True
	elif number in nonAbundantInventory:
		return False
	else:
		if sumFactors(number) > number:
			abundantInventory.add(number)
			return True
		else:
			nonAbundantInventory.add(number)
			return False

total = 0
abundantNums = set([])
nonAbundantNums = set([])
for number in range(1,28124):
	#print number
	summand = 1
	upperLimit = number/2
	canBeWrittenAsSumOfTwoAbundantNumbers = False
	while summand <= upperLimit:
		if isAbundant(summand,abundantNums,nonAbundantNums) and isAbundant(number - summand,abundantNums,nonAbundantNums):
			canBeWrittenAsSumOfTwoAbundantNumbers = True
			break
		summand += 1
	if not canBeWrittenAsSumOfTwoAbundantNumbers:
		total += number
print(total)
