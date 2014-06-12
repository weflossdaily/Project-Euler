def countDescending(prefix,numDigits):
	count = 0
	if numDigits > 1:
		for i in range(int(prefix[len(prefix) - 1]) + 1):
			count += countDescending(prefix + str(i),numDigits - 1)
	else:
		#for i in range(int(prefix[len(prefix) - 1]) + 1):
		#	print prefix + str(i)
		return int(prefix[len(prefix) - 1]) + 1
	return count

def countAscending(prefix,numDigits):
	count = 0
	if numDigits > 1:
		for i in range(int(prefix[len(prefix) - 1]),10):
			count += countAscending(prefix + str(i),numDigits - 1)
	else:
		#for i in range(int(prefix[len(prefix) - 1]),10):
		#	print prefix + str(i)
		return len(range(int(prefix[len(prefix) - 1]),10))
	return count

digits = 100
print 2*countDescending('9',digits) -10 -1