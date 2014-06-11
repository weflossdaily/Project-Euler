"""14:04:10  REID POWELL : I wonder if rust's match could help solve problem 113 really quickly
14:12:14  RUTVIJ BHATT : What's problem 113?
14:12:51  REID POWELL : https://projecteuler.net/problem=113
14:14:49  RUTVIJ BHATT : This sounds like it's a formula where # of digits is a variable
14:16:00  REID POWELL : ok I feel you
14:16:52  REID POWELL : like:
for k from 1 to 100 do
    count how many bouncy #'s with k digits?
14:18:05  RUTVIJ BHATT : Think this is a combinatorics problem where you add up all possible ways to make a non-bouncy number?
14:18:11  REID POWELL : love it
14:18:33  REID POWELL : that feels like a good approach
14:18:48  REID POWELL : recursion?
14:19:18  REID POWELL : makeBouncy(firstDigitMax,numDigits)
14:19:36  REID POWELL : sorry makeNonBouncy
14:20:47  RUTVIJ BHATT : I think I'm talking out of my ass. I can't think of a way to add this up reasonably ATM
14:22:33  REID POWELL : .
def countDecreasing(firstDigitMax,numDigits):
    countDecreasing(9,numDigits - 1) + countDecreasing(8,numDigits - 1) +...
14:23:14  REID POWELL : I guess we need an if in there to see how big numDigits is
14:23:53  REID POWELL : def countDecreasing(firstDigitMax,numDigits):
    if numDigits > 1:
        countDecreasing(9,numDigits - 1) + countDecreasing(8,numDigits - 1) +...
    else:
14:24:07  REID POWELL : .
    return firstDigitMax
14:24:48  REID POWELL : and the '9' in the numDigits > 1 case should start at firstDigitMax instead
14:25:36  RUTVIJ BHATT : That seems pretty good
14:25:56  REID POWELL : then we say print str(countDecreasing(9,100) + countIncreasing(9,100))
14:26:17  REID POWELL : sorry, I guess countIncreasing(1,100)
14:26:37  REID POWELL : thanks for the approach!
14:30:56  REID POWELL : gonna put this convo in the comments """

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

digits = 2
print countDescending('9',digits) + countAscending('0',digits)
