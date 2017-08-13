'''
import time;

tInterval = 15;
tStart = time.time();

isPrime = 1;
primeSum = 2;
i = 3;

while i < 2000000:
    if time.time() - tStart > tInterval:
        print "at num: %i" % i;
        tStart = time.time();
    j = 2
    while j < i:
        if i%j == 0:
           isPrime = 0;
           break;
        j += 1;
    if isPrime:
        primeSum += i;
    else:
        isPrime = 1;
    i += 2;
    

print primeSum;


'''
numMax = 2000000;

nums = [1]*numMax;
print "array init";
i = 2;

while i < len(nums):
    if nums[i-1] == 1:
        j = 2*i;
        while j <= len(nums):
            nums[j-1] = 0;
            j += i;
    i += 1;
print "sieved"
primeSum = 0;

i = 1;

while i < len(nums):
    if nums[i] == 1:
        primeSum += i+1;
    i += 1;
print primeSum;
