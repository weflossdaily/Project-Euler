#!/opt/swt/bin/python
import sys

i = 1
while True:
	eye = ''.join(sorted(str(i)))
	if ''.join(sorted(str(6 * i))) == eye:
		if ''.join(sorted(str(5 * i))) == eye:
			if ''.join(sorted(str(4 * i))) == eye:
				if ''.join(sorted(str(3 * i))) == eye:
					if ''.join(sorted(str(2 * i))) == eye:
						print str(i)
						break
	i+=1
