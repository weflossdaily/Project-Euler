import math


        
        
n=1000000000000
while True:
    limit=.707107782*n
    i=.70710778*n 
    while i<limit:
        if (i*(i-1))/(n*(n-1))==.5:
            print str(i)
        i+=1
    n+=1
        
        
        
        
        
n=1000000000000
a=.5*(math.sqrt((2*n)*(n-1)+1)+1)
while a!=math.floor(a):
    n+=1
    a=.5*(math.sqrt((2*n)*(n-1)+1)+1)
print str(math.floor(a))
print str(n)
print str((a*(a-1))/(n*(n-1)))

i=707106783000
while True:
    i+=1
    if (i*(i-1))/(1000000002604*1000000002603)==.5:
        print str(i)
