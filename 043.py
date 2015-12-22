from itertools import combinations

primes = [2,3,5,7,11,13,17]
total = [0]

def recursion(remainingDigits,prefixDigits, total):
    for digitTuple in combinations(remainingDigits,1):
        digit = digitTuple[0]
        numUsedDigits = len(prefixDigits)

        # no leading zeros
        if digit == 0 and numUsedDigits == 0: # there has to be a better way
            continue

        # warmup
        elif numUsedDigits < 3:
            recursion([x for x in remainingDigits if x != digit],prefixDigits + [digit], total)

        # start checking the digit-window for divisibility by the appropriate prime
        else:
            currentPrime = primes[numUsedDigits - 3]
            strDigit = str(digit)
            if int(''.join([str(x) for x in prefixDigits])[-2:] + strDigit) % currentPrime == 0:
                # the current digit-window-tuplet is divisible by the appropriate prime
                if numUsedDigits == 9:
                    # got there
                    total[0] += int(''.join([str(x) for x in prefixDigits]) + strDigit)
                else:
                    # not there yet; keep working
                    recursion([x for x in remainingDigits if x != digit],prefixDigits + [digit],total)

recursion(range(10),[],total)
print(total)