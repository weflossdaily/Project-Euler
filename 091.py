#!/opt/swt/bin/python

numTriangles = 0

for x1 in range(0,51):
	for y1 in range(0,51):
		# let the counterclockwise-most leg of the triangle terminate anywhere,
		# but ensure the other let is more clockwise to avoid double counting
		# a.k.a. if y2-y1 >= (y1/x1)(x2-x1), continue
		for x2 in range(0,51):
			for y2 in range(0,51):
				# if the counterclockwise-most leg is vertical, handle it
				if x1 == 0:
					if y1 == 0:
						# degeneracy: p1 is origin, no triangle
						continue
					if x2 == 0:
						# degeneracy: legs are on top of each other, no triangle
						continue
					if y2 == 0:
						# one vertical leg and one horizontal leg (with positive length)
						numTriangles += 1 # *
						continue
					# legs aren't perpendicular, not a right triangle
					continue
				# does p1 determine counterclockwise-most leg?
				if y2-y1 >= (y1/x1)*(x2-x1):
					# no it doesn't
					# print(y2-y1,(y1/x1)*(x2-x1),x1,y1,x2,y2)
					continue
				else:
					# we actually have a triangle!
					# make 3 comparisons: each leg with each other
					# 1. (O,p1) witt (O,p2)
					#    This is no longer needed, since these form a right
					#    triangle only when on y- and x- axes respectively and
					#    this comparison was made at *
					# 2. (O,p1) with (p1,p2)
					if (x1*(x1-x2)) == (y1*(y2-y1)):
						numTriangles += 1
						continue
					# 3. (p1,p2) with (p2,O)
					if (x2*(x2-x1)) == (y2*(y2-y1)):
						numTriangles += 1
						continue
					continue

print(numTriangles)
