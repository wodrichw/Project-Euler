int result = int.MaxValue;
primes = ESieve(30000);
HashSet[] pairs = new HashSet[primes.Length];
 
for (int a = 1; a < primes.Length; a++) {      if (primes[a] * 5 >= result) break;
    if (pairs[a] == null) pairs[a] = MakePairs(a);
    SortedSet testSet = new SortedSet(pairs[a]);
 
    for (int b = a + 1; b < primes.Length; b++) { 
         if (primes[a] + primes[b] * 4 >= result) break;
        if (!testSet.Contains(primes[b])) continue;
        if (pairs[b] == null) pairs[b] = MakePairs(b);
        SortedSet tempA = new SortedSet(testSet);
        testSet.IntersectWith(pairs[b]);
        if (testSet.Count == 0) {
            testSet = tempA;
            continue;
        }
 
        for (int c = b + 1; c < primes.Length; c++) { 
             if (primes[a] + primes[b] + primes * 3 >= result) break;
            if (!testSet.Contains(primes)) continue;
            if (pairs == null) pairs = MakePairs(c);
            SortedSet tempB = new SortedSet(testSet);
            testSet.IntersectWith(pairs);
            if (testSet.Count == 0) {
                testSet = tempB;
                continue;
            }
 
            for (int d = c + 1; d < primes.Length; d++) { 
                 if (primes[a] + primes[b] + primes + primes[d] * 2 >= result) break;
                if (!testSet.Contains(primes[d])) continue;
                if (pairs[d] == null) pairs[d] = MakePairs(d);
                SortedSet tempC = new SortedSet(testSet);
                testSet.IntersectWith(pairs[d]);
                if (testSet.Count == 0) {
                    testSet = tempC;
                    continue;
                }
 
                int e = testSet.Min;
 
                if (primes[a] + primes[b] + primes + primes[d] + e < result)
                    result = primes[a] + primes[b] + primes + primes[d] + e;
 
                Console.WriteLine("{0} + {1} + {2} + {3} + {4} = {5}", primes[a], primes[b], primes, primes[d], e, result);
 
                testSet = tempC;
            }
            testSet = tempB;
        }
        testSet = tempA;
    }
}
