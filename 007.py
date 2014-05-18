def isPrime(number,primes):
    for i in range(0,len(primes)):
        if number % primes[i] == 0:
            return
    primes.append(number)

primes = []
for i in range(2,104744):
    isPrime(i,primes)
print str(primes[len(primes)-1])