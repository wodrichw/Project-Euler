import time


primeNum = 10001;
primes = [2,3];
i = 4;
isPrime = 1;
maxTime = 30;
start = time.time();
end = start;

while end - start < maxTime:
    for j in range(len(primes)):
        if i%primes[j] == 0:
           isPrime = 0;
           break;
    if isPrime:
        primes.append(i);
    else:
        isPrime = 1;
    i += 1;
    end = time.time();

print "%ith prime: %i" % (len(primes), primes[len(primes)-1]);
print primes;
