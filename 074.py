import math
# could probably be faster by maintaining some structure with distances for that last bit, similar to the problem that stopped at 576

def getNextLink(n):
    sum=0
    for digit in str(n):
        sum+=math.factorial(int(digit))
    return sum

def countNonRepeats(n):
    terms = set([n])
    n = getNextLink(n)
    while not n in terms and len(terms) < 62:
        terms.add(n)
        n=getNextLink(n)
    return len(terms)

i = 1
count = 0
while i < 1000000:
    #print str(i) + ' has ' + str(countNonRepeats(i))
    if countNonRepeats(i)==60:
        count += 1
    i+=1
print str(count)
