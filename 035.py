thisMany = 1000000+1

def unprimeIndices(number,primality):
    leng = thisMany
    currentIndexToUnprime=2*number 
    while currentIndexToUnprime < leng:
        primality[currentIndexToUnprime]=0
        currentIndexToUnprime+=number 

def findNextPrime(lastPrimeIndex,primality):
    leng = thisMany
    currentIndex=lastPrimeIndex+1
    while currentIndex < leng and primality[currentIndex]==0:
        currentIndex+=1
    return currentIndex

def printPrimes(primality):
    for i in range(2,thisMany):
        if primality[i]==1:
            print str(i) + ', '

def sumPrimes(primality):
    sum=0
    for i in range(2,thisMany):
        if primality[i]==1:
            sum+=i 
    print str(sum)

def isPrime(number,primes):
	if primes[number] == 1:
		return True
	else:
		return False

def permuteNumString(numString):
	return numString[len(numString)-1] + numString[:-1]

def isCircularPrime(number,primes):
	numString = str(number)
	if isPrime(number,primes):
		newString = permuteNumString(numString)
		while newString != numString:
			if not isPrime(int(newString),primes):
				return False
			newString = permuteNumString(newString)
	else:
		return False
	return True

primalities=[1]*thisMany
#why len give int not callable error
leng= thisMany
currentPrime=2
while currentPrime < leng:
    unprimeIndices(currentPrime,primalities)
    currentPrime=findNextPrime(currentPrime,primalities)
print 'got primes'
count = 0
# get primes, since current function requires all earlier primes
for i in range(2,1000001):
	if isCircularPrime(i,primalities):
		print i
		count += 1
print count
