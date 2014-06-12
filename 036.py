def isPalindromic(numberString):
	length = len(numberString)
	halfway = length/2
	i = 0
	while i <= halfway:
		if numberString[i] != numberString[length - i]:
			return False
	return True

def convertBase10To2(number):

total = 0
i = 0
while i < 1000000:
	i+=1
	if isPalindromic(str(i)) and isPalindromic(convertBase10To2(i)):
		print str(i) + ', ' + convertBase10To2(i)
		total += i
print total
