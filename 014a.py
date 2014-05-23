import math

def measureSequence(n,seq):
    term = n
    seq.append(term)
    terms = 1
    while term !=1:
        terms+=1
        half = term/2.0
        if half == math.floor(half):
            term=half
        else:
            term=3*term+1
        seq.append(term)

maxTerms=0
i=1
startingNumber = i
newLength=0
while i<1000000:
    terms=[]
    measureSequence(i,terms)
    newLength=len(terms)
    if newLength > maxTerms:
        maxTerms = newLength
        startingNumber = i 
    i+=1
    if i%100000==0:
        print terms
print str(startingNumber)