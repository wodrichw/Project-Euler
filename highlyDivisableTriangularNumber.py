
'''

##create array with 1 for prime, 0 for not prime at indext of num-1
numMax = 300000;
nums = [1]*numMax;
i = 2;

while i < len(nums):
    if nums[i-1] == 1:
        j = 2*i;
        while j <= len(nums):
            nums[j-1] = 0;
            j += i;
    i += 1;


primes = nums[:];
for i in range(len(primes)):
    if primes[i] != 0: primes[i] = i + 1;

primes.pop(0); ##delets 1 from list of primes

i = 0;
while i < len(primes):
    if primes[i] == 0:
        primes.pop(i);
    else:
        i += 1;

print"primes initialized";

##Checks if a triangle number has 500 divisors
def highlyDivisable(trinum, primes):
    sqrttri = trinum**0.5
    i = 0;
    dvsrCount = 2; ##every number is divisable by 1 and itself


    while i < len(primes) and primes[i] < sqrttri:
        temp = trinum;
        while temp%primes[i] == 0:
            dvsrCount += 1;
            temp = temp/primes[i];
        if dvsrCount >= 500:
            return True;
        i += 1;

    if primes[len(primes)-1] <= sqrttri:
        print"we ran out of primes....";
    if dvsrCount > 200:
        print"Divisor Count: %i, num: %i" % (dvsrCount,  trinum);
    return False;

##Run through all triangle numbers until we reach one that has 500 divisors
n = 22;
trinum =  n*(n-1)/2;
while not highlyDivisable(trinum + n, primes):
    n += 1;


##Print the Tiangle Number
print(n*(n+1)/2);


'''




##We will assume the triangle number is less than million
nums = [0]*1000000

n = 2;
trinum = 1;

while trinum < len(nums):
    nums[trinum] = 1;
    trinum += n;
    n += 1;

print "trinums placed";


##add divisor counts to tri nums
for n in range(2, len(nums)):
    i = n;
    while i < len(nums):
        if not nums[i] == 0:
            nums[i] += 1;
            if nums[i] > 50:
                print "tri num: %i, div: %i" %(i, nums[i]);
            i += n;
    
