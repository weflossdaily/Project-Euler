number = 2
while True:
	#print number
	digits = str(number)
	fifthPowerDigitSum = 0
	for digit in digits:
		#print fifthPowerDigitSum
		fifthPowerDigitSum+=((int(digit))**5)
		if fifthPowerDigitSum > number:
			break
	if fifthPowerDigitSum == number:
		print number
	number += 1
