def isBouncy(num):
	digits = str(num)
	direction = 0
	numDigits = len(digits)
	# print digits + ', ' + str(numDigits)
	for i in range(1,numDigits):
		if int(digits[i-1]) < int(digits[i]):
			# print digits[i-1] + ' < ' + digits[i]
			if direction < 0:
				return True
			elif direction > 0:
				continue
			else:
				direction = 1
				# print 'direction is now increasing'
		if int(digits[i-1]) > int(digits[i]):
			# print digits[i-1] + ' > ' + digits[i]
			if direction < 0:
				continue
			elif direction > 0:
				return True
			else:
				direction = -1
				# print 'direction is now decreasing'
	return False

def is99Percent(num,denom):
	#print str(num) + ', ' + str(denom)
	if ((denom * 99) == (num * 100)):
		return True
	return False

num = 0
denom = 0
i = 0
while True:
	i+=1
	denom += 1
	if isBouncy(i):
		num += 1
	if is99Percent(num, denom):
		print str(i)
		break