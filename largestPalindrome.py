pallen =  [];
pallenflag = 0;
insertflag = 0;

for i in range(100, 1000):
    for j in range(i + 1, 1000):
        product = i*j;
        prodString = str(product);
        for k in range(len(prodString)/2):
            if prodString[k] != prodString[len(prodString)-1-k]:
                pallenflag = -1;
                break;
        if pallenflag == 0:
                for k in range(len(pallen)):
                    if product == pallen[k]:
                        break;
                    if product < pallen[k] :
                        pallen.insert(k, product);
                        insertflag = -1;
                        break;
                if insertflag == 0:
                    pallen.append(product);
                else:
                    insertflag = 0;
        else:
            pallenflag = 0;

print "Final List : ", pallen;
