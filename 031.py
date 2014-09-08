def countWays(amt,denominations):
    #print(amt,denominations)
    if amt <=0 or len(denominations) == 1:
        return 1
    ways = 0
    biggestCoin = denominations[0]
    i = amt//biggestCoin
    #print(i)
    while i >= 0:
        ways += countWays(amt-i*biggestCoin,denominations[-(len(denominations)-1):])
        i -= 1
        #print(ways)
    return ways

denominations = [200,100,50,20,10,5,2,1]

print(countWays(200,denominations))
