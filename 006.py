#!/opt/swt/bin/python
import sys

inside = 0
outside = 0

for i in range(0,100 + 1):
	inside += (i * i)
	outside += i
	# print str(i) + ', ' + str(inside) + ', ' + str(outside)

print str(((outside * outside) - inside))
