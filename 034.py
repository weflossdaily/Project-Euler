number = 2
factorials = [1]
for i in range(1,10):
	factorials.append(factorials[i-1] * i)

print factorials

total = 0
while True:
	number += 1
	digits = str(number)
	digitSum = 0
	for digit in digits:
		digitSum += factorials[int(digit)]
	if number == digitSum:
		print number
		total += number
		print total
