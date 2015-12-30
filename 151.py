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
