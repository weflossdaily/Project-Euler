#!/opt/swt/bin/python
import sys

previousTerm = 2
previousPreviousTerm = 1
currentTerm = previousTerm + previousPreviousTerm
sum = 2
while currentTerm <= 4000000:
	if currentTerm%2 == 0:
		sum += currentTerm
	previousPreviousTerm = previousTerm
	previousTerm = currentTerm
	currentTerm = previousTerm + previousPreviousTerm
print sum
