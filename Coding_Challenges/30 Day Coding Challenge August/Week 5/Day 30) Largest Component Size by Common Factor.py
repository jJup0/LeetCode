from collections import defaultdict
from math import sqrt
# decent but too slow


class Solution:
    def largestComponentSize(self, A: [int]) -> int:
        factorDict = defaultdict(set)
        numFactors = defaultdict(set)
        primes = []  # generate primes
        for potentialPrime in range(2, max(10, max(A)//2)):
            for divisor in range(2, 1 + potentialPrime//2):
                if potentialPrime % divisor == 0:
                    break
            else:
                primes.append(potentialPrime)
        # create dicts for prime to number and number to prime
        for n in A:
            factorDict[n].add(n)
            numFactors[n].add(n)
            for f in primes:
                if not n % f:  # range(2, 1+ n//2)
                    factorDict[f].add(n)
                    numFactors[n].add(f)
        # find longest chain
        res = 1
        while len(numFactors):
            n, fqueue = numFactors.popitem()
            for f in fqueue:
                factorDict[f].remove(n)
            chain = set()
            while fqueue:
                f = fqueue.pop()
                for n in factorDict[f]:
                    fqueue.update(numFactors[n])
                    numFactors[n].clear()
                chain.update(factorDict[f])
                factorDict[f].clear()
            res = max(res, len(chain)+1)
        return res
