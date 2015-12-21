from math import factorial
def recurse(lowerBound,upperBound,numberOfRedDiscs,sumSoFar,intermediateProduct):
	if numberOfRedDiscs > (upperBound - lowerBound) or numberOfRedDiscs <= 0:
		if numberOfRedDiscs == 0:
			sumSoFar[0] += intermediateProduct
		return sumSoFar

	sumSoFar[0] += intermediateProduct

	for i in range(lowerBound + 1,upperBound + 1):
		recurse(i,upperBound,numberOfRedDiscs - 1,sumSoFar,intermediateProduct * i)[0]
	return sumSoFar

sumSoFar = recurse(
	1,   # first turn
	15,   # last turn
	7,   # most red discs you can pull and still win
	[0], # Haven't accumulated any counts yet
	1)   # Haven't counted any ways to pull a red disc on turn i yet
print(sumSoFar[0]/factorial(15 + 1))