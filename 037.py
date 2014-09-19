thisMany = 2000000+1

def unprimeIndices(number,primality):
    leng = thisMany
    currentIndexToUnprime=2*number 
    while currentIndexToUnprime < leng:
        primality[currentIndexToUnprime]=0
        currentIndexToUnprime+=number

def isTrunctable(prime,primalities):
    primeString = str(prime)
    for i in range(1,len(str(prime))):
        if primalities[int(str(prime)[i:])] == 0 or primalities[int(str(prime)[:(len(str(prime))-i)])] == 0:
            return False
    return True

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

primalities=[1]*thisMany
primalities[0] = 0
primalities[1] = 0
#why len give int not callable error
leng= thisMany
currentPrime=2
numTrunctable = 0
total = 0
while numTrunctable < 11:
    if currentPrime > 7:
        if isTrunctable(currentPrime,primalities):
            numTrunctable += 1
            total += currentPrime
            # print str(currentPrime) + ' isTrunctable'
    unprimeIndices(currentPrime,primalities)
    currentPrime=findNextPrime(currentPrime,primalities)
print total
