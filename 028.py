term = 1
total = term
sideLength = 2
for i in range(0,500):
	for j in range(0,4):
		term+=sideLength
		total+=term
	sideLength+=2
print total
