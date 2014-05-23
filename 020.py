import math

sum=0
for char in str(math.factorial(100)):
	sum += int(char)
print str(sum)