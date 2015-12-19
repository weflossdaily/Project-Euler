def unprimeIndices(number,primality):
    leng = len(primality)
    currentIndexToUnprime=2*number 
    while currentIndexToUnprime < leng:
        primality[currentIndexToUnprime]=0
        currentIndexToUnprime+=number 

def findNextPrime(lastPrimeIndex,primality):
    leng = len(primality)
    currentIndex=lastPrimeIndex+1
    while currentIndex < leng and primality[currentIndex]==0:
        currentIndex+=1
    return currentIndex

primality = [1]*999983
primality[0]=0
primality[1]=0
currentPrime=2
while currentPrime < len(primality):
    unprimeIndices(currentPrime,primality)
    currentPrime=findNextPrime(currentPrime,primality)

primes = []
primeSet = set()
for i in range(len(primality)):
    if primality[i]==1:
        primes.append(i)
        primeSet.add(i)

windowSize = 22
while windowSize < 78000:
    for start in range(len(primes)-windowSize):
        if sum(primes[start:start+windowSize-1]) in primeSet:
            print(sum(primes[start:start+windowSize-1]))
            break
    windowSize+=1
    if windowSize % 1000 == 0:
        print(windowSize)