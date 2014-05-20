import math

sum = 0
i = 2
perimeter = 3*i+1
print 'going'
while perimeter<1000000000:
    # this area expression can probably get quicker since last iteration we already did some of the work
    area = .25*math.sqrt(i*(i*(i*(3*i+4)-2)-4)-1)
    # area = .25*math.sqrt(((i+1)**2)*(i-1)*perimeter)
    
    # is the area integral?
    if area == math.floor(area):
    	#print str(perimeter) + ': ' + str(i) + ', ' + str(i) + ', ' + str(i+1) + ': ' + str(area)
        sum+=(perimeter)
    
    # on to the next triangle!
    i+=1
    perimeter = 3*i+1

print str(sum)
