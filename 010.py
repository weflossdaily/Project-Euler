thisMany = 2000000+1

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

primalities=[1]*thisMany
#why len give int not callable error
leng= thisMany
currentPrime=2
while currentPrime < leng:
    unprimeIndices(currentPrime,primalities)
    currentPrime=findNextPrime(currentPrime,primalities)
sumPrimes(primalities)