def countFactors(number):
    numFactors = 2 # 1 and itself
    i=2
    limit = (number/2) + 1
    while i < limit:
        #print 'limit is ' + str(limit) + ', i is ' + str(i)
        if number%i==0:
            limit = (number/i) + 1
            if i < (number/i):
                #print str(number) + ' is divisible by ' + str(i) + ' and ' + str(number/i)
                numFactors += 2
            elif (i*i) == number:
                #print str(number) + ' is divisible by ' + str(i)
                numFactors += 1
        #else:
            #print str(number) + ' is not divisible by ' + str(i)
        i += 1
    return numFactors

currentTriangularNumber = 0
numFactors = 0
i = 1
while numFactors < 500:
    currentTriangularNumber += i
    i += 1
    numFactors = countFactors(currentTriangularNumber)
print str(currentTriangularNumber) + ', ' + str(numFactors)