previousPreviousTerm = 1
previousTerm = 1
currentTerm = previousPreviousTerm + previousTerm
i=3
while len(str(currentTerm)) < 1000:
    previousPreviousTerm = previousTerm
    previousTerm = currentTerm
    currentTerm = previousPreviousTerm + previousTerm
    i+=1
print str(i)
