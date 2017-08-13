for a in range(500):
    for b in range(500):
        c = 1000 - a - b;
        if c*c == a*a + b*b:
            break;
    if c*c == a*a + b*b:
        break;

print ("Pythagorian Triple: %i, %i, %i" % (a, b, c));
print "product: %i" % (a*b*c);
