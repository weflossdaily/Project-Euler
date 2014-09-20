# referred to http://mathworld.wolfram.com/PartitionFunctionq.html
Pnm = []

def calculatePnm(n,m):
	if m > n:
		return 0
	if m == n:
		return 1
	if m == 0:
		return 0
	return calculatePnm(n,m-1) + calculatePnm(n-m,m)

n=0
m=0
while 1:
