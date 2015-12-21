from math import factorial
from math import floor
from math import ceil
from itertools import chain
from itertools import combinations

numberOfPulls = 15
maxRedPulls = ceil((numberOfPulls / 2) - 1)
waysToWinSoFar = 0
waysToPlay = factorial(numberOfPulls + 1)

# from https://docs.python.org/2/library/itertools.html
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

games = powerset(range(1,numberOfPulls + 1))
for redPulls in games:
	if len(redPulls) > maxRedPulls:
		break
	product = 1
	for pull in redPulls:
		product *= pull
	waysToWinSoFar += product

print(floor(waysToPlay/waysToWinSoFar))