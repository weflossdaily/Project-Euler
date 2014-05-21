import math

def measureSequence(n):
    term = n
    terms = 1
    while term !=1:
        terms+=1
        half = term/2
        if half == math.floor(half):
            term=half
        else:
            term=3*term+1
    return terms       

maxTerms=0
i=1
startingNumber = i
newLength=0
while i<1000000:
    newLength = measureSequence(i)
    if newLength > maxTerms:
        maxTerms = newLength
        startingNumber = i 
print str(startingNumber)