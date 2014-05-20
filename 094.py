import math

sum = 0
i = 1
perimeter = 3*i+1
while perimeter<10000000001:
    # this area expression can probably get quicker since last iteration we already did some of the work
    area = .25*math.sqrt(i*(i*(i*(3*i+4)-2)-4)-1)
    if area == math.floor(area):
        sum+=(perimeter)
    i+=1
    perimeter = 3*i+1
print str(sum)
