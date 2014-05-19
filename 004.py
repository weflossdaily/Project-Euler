#!/opt/swt/bin/python
import sys
import math

def isPalindrome(number):
	stringRepresentation = str(number)
	stringLength = len(stringRepresentation)
	for i in range(0,math.floor(stringLength/2)):
		if not stringRepresentation[i] == stringRepresentation[stringLength - i - 1]:
			return False
	print stringRepresentation # + ' is a palindrome'
	return True

def findGreatestPalindrome(maxInt):
	for i in range(0,2*maxInt + 1):
		for j in range(0,i + 1):
			if isPalindrome((maxInt - i + j) * (maxInt - i - j)):
				print str((maxInt - i + j)) + ', ' + str((maxInt - i - j))
				return

findGreatestPalindrome(999)
