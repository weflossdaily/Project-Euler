def harvestAttempt(sheetsInHand):
    if sheetsInHand.count(5) > 0:
        # Have an A5 and took it
        sheetsInHand.remove(5)
        return sheetsInHand
    else:
        # pull the smallest sheet and cut it up
        smallestSheet = max(sheet for sheet in sheetsInHand)
        sheetsInHand.remove(smallestSheet)
        oneHalf = smallestSheet + 1
        return harvestAttempt(sheetsInHand + [oneHalf,oneHalf])

expectation = [0]
def recursion(inventory,numLuckyPulls,parentProbability,expectation):
    
    if inventory == [5]:
        return ((numLuckyPulls + len(inventory) - 1) * parentProbability)
    
    if len(inventory) == 1:
        expectation[0] += parentProbability
    
    expectedPulls = 0
    for sheetSize in inventory: #set(inventory):
        #probability = inventory.count(sheetSize)/len(inventory)
        probability = 1/len(inventory)
        # print("Suppose that I pulled, with probability",probability,", a sheet size of",sheetSize,", having",numLuckyPulls,"lucky pulls so far with a total probability of",parentProbability * probability)
        inventory.remove(sheetSize)
        if sheetSize == 5:
            # print(inventory)
            expectedPulls += recursion(inventory, numLuckyPulls + 1, parentProbability * probability,expectation)
        else:
            # print(inventory + cutToSizeTheSmallestOf([sheetSize]))
            expectedPulls += recursion(inventory + harvestAttempt([sheetSize]), numLuckyPulls, parentProbability * probability,expectation)
    return expectedPulls
