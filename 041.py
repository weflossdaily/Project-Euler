thisMany = 100000000+1

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

def isPandigital(number):
    numString = sorted(str(number))
    # print(numString)
    for i in range(len(numString)):
        if numString[i] != str(i+1):
            return False
    return True

print('starting primes')
primalities=[1]*thisMany
#why len give int not callable error
leng = thisMany
currentPrime=2
while currentPrime < leng:
    unprimeIndices(currentPrime,primalities)
    currentPrime=findNextPrime(currentPrime,primalities)

print('done with primes')

print(isPandigital(12346785))

#print(primalities)
for i in range(2,len(primalities)):
    if primalities[i] == 1:
        if isPandigital(i):
            print(i)