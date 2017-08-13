import math;
x = 20
fact = math.factorial(x);
lcm = fact;
lcmPossible = lcm;
canReduce = 1;

print fact;


for i in range(x+1):
    if i != 0:
        lcmPossible = lcm/i;
        for j in range(x+1):
            if j != 0 and lcmPossible%j != 0:
                lcmPossible = -1;
                break;
        if lcmPossible != -1:
            lcm = lcmPossible;
            print "i: %i, lcm: %i" % (i, lcm)
        else:
            lcmPossible = lcm;
