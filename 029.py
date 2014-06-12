import math

sequence = set([])
for a in range(2,101):
	for b in range(2,101):
		sequence.add(a**b)
print len(sequence)
