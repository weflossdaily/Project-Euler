def endsAt89(n,targets,misses):
    while(True):
        #print str(n)
        if n in targets:
            return True
        elif n in misses:
            return False
        else:
            n=getNextDigit(n)
        
def getNextDigit(n):
    sum=0
    for char in str(n):
        sum+=(int(char))**2
    return sum

total=0
targets=set([89])
misses=set([1])
for i in range(1,567):
    if endsAt89(i,targets,misses):
        targets.add(i)
        #print str(i) + ' ends at 89'
        total+=1
    else:
        misses.add(i)
for i in range(567,10000000):
    if endsAt89(i,targets,misses):
        #print str(i) + ' ends at 89'
        total+=1
print str(total)