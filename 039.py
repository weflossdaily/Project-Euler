#gonna exhaustively search, if that's a problem, we'll be smarter by only exploring triplets that yield triangles
import math
maxSolutions = 0
bestP = 0
for p in range(1,1001):
	numSolutionsForThisP = 0
	# print(range(1,p+1))
	for hypotnuse in range(1,math.ceil(p/2)):
		for longLeg in range(int(math.floor(p/4)),int(math.ceil(p/2)+ 1)):
			shortLeg = p - hypotnuse - longLeg
			if longLeg + shortLeg > hypotnuse:
				# print(p,hypotnuse,longLeg,shortLeg)
				if (hypotnuse * hypotnuse) == (longLeg * longLeg + shortLeg * shortLeg):
					numSolutionsForThisP += 1
				if numSolutionsForThisP > maxSolutions:
					maxSolutions = numSolutionsForThisP
					bestP = p
print(bestP)