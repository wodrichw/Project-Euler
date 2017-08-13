import math
x = 600851475143;
i = 1;
factors = [];
primefactors = [];
flag = 0;

while i < math.sqrt(x):
    if x%i == 0:
        factors.append(i);
    i += 1;

'''

for i in range(2, len(factors)):
    for j in range(i, len(factors)):
        if factors[j]%factors[i]:
            factors.pop(i);
            i -= 1;
            break;
        
for i in range(len(factors)):
    for j in range(i, len(factors)):
        if j != i and factors[i]%factors[j] == 0:
            flag = -1;
    if flag == 0:
        primefactors.append(factors[i]);
    else:
        flag = -1;

'''

for i in range(len(factors)):
    if i < len(factors) and factors[i] == 1:
        factors.pop(i);
        i -= 1;
    else:
        for j in range(i + 1, len(factors)):
            if j < len(factors) and factors[j]%factors[i] == 0:
                factors.pop(j);

for i in range(len(factors)):
    print " %i" % factors[i];
