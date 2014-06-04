cost = [0]
inFile = open("018.in", "rw+")
for line in inFile:
	# print "cost: " + str(cost)
	i = 0
	newCost = []
	nodes = line.split()
	for node in nodes:
		if i == 0:
			newCost.append(cost[i] + int(nodes[i]))
		elif i == len(nodes) - 1:
			newCost.append(cost[len(cost) - 1] + int(nodes[i]))
		else:
			newCost.append(max(cost[i-1],cost[i]) + int(nodes[i]))
		i += 1
	cost = newCost
print max(cost)