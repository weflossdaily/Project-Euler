import math

sum = 0
i = 1

while 3*i+1<10000000001:
    a=i 
    b=i 
    c=i+1
    area = .25*math.sqrt((-a+b+c)*(a-b+c)*(a+b-c)*(a+b+c))
    if area == math.floor(area):
        sum+=(a+b+c)
    i+=1
print str(sum)
