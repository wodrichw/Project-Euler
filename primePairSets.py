import sympy

##create array with 1 for prime, 0 for not prime at indext of num-1
numMax = 10000000;
nums = [1]*numMax;
i = 2;

while i < len(nums):
    if nums[i-1] == 1:
        j = 2*i;
        while j <= len(nums):
            nums[j-1] = 0;
            j += i;
    i += 1;


'''
##create hash table of primes
primes = nums[:30000];
for i in range(len(primes)):
    if primes[i] != 0: primes[i] = i + 1;

primes.pop(0); ##delets 1 from list of primes

i = 0;
while i < len(primes):
    if primes[i] == 0:
        primes.pop(i);
    else:
        i += 1;
'''
print "primes initialized";

'''
primePairs = set([]);
def checkPair(p1, p2, nums):
    if int(str(p1) + str(p2)) > max(nums) or int(str(p2) + str(p1)) > max(nums):
        notPrime = 0;
        for i in range(1, len(nums)):
            if nums[i] == 1 and (int(str(p1) + str(p2))%(i + 1) == 0 or int(str(p2) + str(p1))%(i+1) == 0):
                notPrime = 1;
                break;
        if notPrime == 0:
            return 1;
        else:
            return 0;
    elif nums[int(str(p1) + str(p2)) - 1] == 1 and nums[int(str(p2) + str(p1)) - 1] == 1:
        return 1;
    
    else:
        return 0;

def concat(p1, p2):
    return int(str(p1) + str(p2));

def inPrimePairs(p1, p2, primePairs):
    if concat(p1, p2) in primePairs or concat(p2, p1) in primePairs:
        return True;
    else:
        return False;

def testPrimes(p, tempPrimes, nums, primePairs):
    for i in range(len(tempPrimes)):
        if not inPrimePairs(p, tempPrimes[i], primePairs):
            if checkPair(p, tempPrimes[i], nums) == 1:
                primePairs.add(concat(p, tempPrimes[i]));
            else:
                return False;
    return True;

for i in range(len(primes)):
    tempI = [primes[i]];
    print "i";
    for j in range(i+1, len(primes)):
        if testPrimes(primes[j], tempI, nums, primePairs):
            tempJ = tempI.append(primes[j]);
            for k in range(j+1, len(primes)):
                print "k";
                if testPrimes(primes[k], tempJ, nums, primePairs):
                    tempK = tempJ.append(primes[k]);
                    for l in range(k+1, len(primes)):
                        print "l";
                        if testPrimes(primes[l], tempK, nums, primePairs):
                            print"i: %i, j: %i, k: %i, l: %i" %(primes[i], primes[j], primes[k], primes[l])
                            tempL = tempK.append(primes[l]);
                            for m in range(l+1, len(primes)):
                                print "m";
                                if testPrimes(primes[m], tempL, nums, primePairs):
                                    print"i: %i, j: %i, k: %i, l: %i, m: %i" %(primes[i], primes[j], primes[k], primes[l], primes[m]);


'''
'''
primes = nums[:30000];


def printPrimes(nums):
    strPrime = "";
    for i in range(len(nums)):
        if nums[i]:
            strPrime += str(i + 1) + ", ";
    print strPrime;

def concat(p1, p2):
    return int(str(p1) + str(p2));


def checkPair(p1, p2, nums):
    if int(str(p1) + str(p2)) > len(nums) or int(str(p2) + str(p1)) > len(nums):
        notPrime = 0;
        for i in range(1, len(nums)):
            if nums[i] == 1 and (int(str(p1) + str(p2))%(i + 1) == 0 or int(str(p2) + str(p1))%(i+1) == 0):
                notPrime = 1;
                break;
        if notPrime == 0:
            return 1;
        else:
            return 0;
    elif nums[int(str(p1) + str(p2)) - 1] == 1 and nums[int(str(p2) + str(p1)) - 1] == 1:
        return 1;

    else:
        return 0;

def sievePrimes(p1, subNums, nums, start):
    for i in range(start, len(subNums)):
        if subNums[i]:
            subNums[i] = checkPair(p1, i + 1, nums);
    return subNums;



smallestSum = -1;
for i in range(1, len(primes)):
    if primes[i]:
        subNums0 = sievePrimes(i+1, primes[:], nums, i+1);
        for j in range(i + 1, len(primes)):
            ##print "j: %i" %j;
            if subNums0[j]:
                subNums1 = sievePrimes(j + 1, subNums0[:], nums, j + 1);
                for k in range(j + 1, len(primes)):
                    if subNums1[k]:
                        ##print "k: %i" %k;
                        subNums2 = sievePrimes(k + 1, subNums1[:], nums, k + 1);
                        for l in range(k + 1, len(primes)):
                            ##print "l: %i" %l;
                            if subNums2[l]:
                                print "i %i, j %i, k %i, l %i" % (i+1, j+1, k+1, l+1);
                                subNums3 = sievePrimes(l + 1, subNums2[:], nums, l + 1);
                                for m in range(l + 1, len(primes)):
                                    if subNums3[m]:
                                        print "i %i, j %i, k %i, l %i, m %i" % (i+1, j+1, k+1, l+1, m+1);
                                        smallestSum = (i+1)+(j+1)+(k+1)+(l+1)+(m+1);
                                        print "sum: %i" %smallestSum;
                                        break;
                            if smallestSum != -1:
                                break;
                    if smallestSum != -1:
                        break;
            if smallestSum != -1:
                break;
    if smallestSum != -1:
        break;
print "smallest sum: %i" % smallestSum;
'''

primes = nums[:30000];
for i in range(len(primes)):
    if primes[i] != 0: primes[i] = i + 1;

primes.pop(0); ##delets 1 from list of primes

i = 0;
while i < len(primes):
    if primes[i] == 0:
        primes.pop(i);
    else:
        i += 1;


def checkPair(p1, p2, nums, primes):
    if int(str(p1) + str(p2)) > len(nums) or int(str(p2) + str(p1)) > len(nums):
        for p in primes:
            if int(str(p1) + str(p2))%p == 0 or int(str(p2) + str(p1))%p == 0:
                return 0;
        return 1;
    elif nums[int(str(p1) + str(p2)) - 1] == 1 and nums[int(str(p2) + str(p1)) - 1] == 1:
        return 1;

    else:
        return 0;

def sievePrimes(p1, subPrimes, nums, primes):
    p1Idx = subPrimes.index(p1);
    if p1Idx + 1 < len(subPrimes):
        i = p1Idx + 1;
        while i < len(subPrimes):
            if checkPair(p1, subPrimes[i], nums, primes) == 0:
                subPrimes.pop(i);
            else:
                i += 1;
    return subPrimes;

i = 0;
tempI = primes[i:];
while i < len(primes):
    tempI = primes[i:];
    tempI = sievePrimes(primes[i], tempI, nums, primes);
    j = 1;
    while j < len(tempI):
        tempJ = tempI[j:];
        tempJ = sievePrimes(tempI[j], tempJ, nums, primes);
        if j >= len(tempJ): break;
        k = 1;
        while k < len(tempJ):
            tempK = tempJ[k:];
            tempK = sievePrimes(tempJ[k], tempK, nums, primes);
            if k >= len(tempK): break;
            l=1;
            while l < len(tempK):
                tempL = tempK[l:]
                tempL = sievePrimes(tempK[l], tempL, nums, primes);
                print"%i %i %i %i" %(tempI[0], tempJ[0], tempK[0], tempL[0]);
                if l >= len(tempL): break;
                m = 1;
                while m < len(tempL):
                    tempM = tempL[m:]
                    tempM = sievePrimes(tempL[l], tempM, nums, primes);
                    print"%i %i %i %i %i" %(tempI[0], tempJ[0], tempK[0], tempL[0], tempM[0]);    
                    m += 1;
                l += 1;
            k += 1;
        j+=1;
    i+= 1;



print primes;
'''
for i in range(1, len(primes)):
    if primes[i]:
        subNums0 = primes[:];
        subNums0 = sievePrimes(i+1, subNums0, nums, i+1);
        for j in range(i + 1, len(primes)):
            ##print "j: %i" %j;
            if subNums0[j]:
                subNums1 = subNums0[:];
                subNums1 = sievePrimes(j + 1, subNums1, nums, j + 1);
                for k in range(j + 1, len(primes)):
                    if subNums1[k]:
                        ##print "k: %i" %k;
                        subNums2 = subNums1[:];
                        subNums2 = sievePrimes(k + 1, subNums2, nums, k + 1);
                        for l in range(k + 1, len(primes)):
                            ##print "l: %i" %l;
                            if subNums2[l]:
                                subNums3 = subNums2[:];
                                print "i %i, j %i, k %i, l %i" % (i+1, j+1, k+1, l+1);
                                subNums3 = sievePrimes(l + 1, subNums3, nums, l + 1);
                                for m in range(l + 1, len(primes)):
                                    if subNums3[m]:
                                        print "i %i, j %i, k %i, l %i, m %i" % (i+1, j+1, k+1, l+1, m+1);
                                        smallestSum = (i+1)+(j+1)+(k+1)+(l+1)+(m+1);
                                        print "sum: %i" %smallestSum;
                                        break;
                            if smallestSum != -1:
                                break;
                    if smallestSum != -1:
                        break;
            if smallestSum != -1:
                break;
    if smallestSum != -1:
        break;
print "smallest sum: %i" % smallestSum;
'''













