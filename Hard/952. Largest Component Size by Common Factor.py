import math
# stolen


class Solution():
    def largestComponentSize(self, A):
        def get_prime_factors(n, primes):  # Prime factor decomposition
            factors = set()
            lim = int(math.sqrt(n))+1
            for p in primes:
                if p > lim:
                    break
                while not n % p:
                    factors.add(p)
                    n //= p
            if n > 2:
                factors.add(n)

            # # to be able to do step = 2
            # while n % 2 == 0:
            #     factors.add(2)
            #     n //= 2
            # for i in range(3, int(math.sqrt(n))+1, 2):
            #     while n % i == 0:
            #         factors.add(i)
            #         n //= i

            return factors

        uf = UnionFind()
        uf.uf(len(A))

        prime_gen = self.gen_primes()
        primes = [next(prime_gen)]

        primeToIndex = {}
        for i, num in enumerate(A):
            lim = math.sqrt(num) + 2
            if primes[-1] < lim:
                while (next_prime := next(prime_gen)) < lim:
                    primes.append(next_prime)
                primes.append(next_prime)

            prime_factors = get_prime_factors(num, primes)
            for p in prime_factors:
                if p in primeToIndex:
                    uf.union(i, primeToIndex[p])
                primeToIndex[p] = i
        return max(uf.size)

    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/

    def gen_primes(self):
        """ Generate an infinite sequence of prime numbers.
        """
        # Maps composites to primes witnessing their compositeness.
        # This is memory efficient, as the sieve is not "run forward"
        # indefinitely, but only as long as required by the current
        # number being tested.
        #
        D = {}

        # The running integer that's checked for primeness
        q = 2

        while True:
            if q not in D:
                # q is a new prime.
                # Yield it and mark its first multiple that isn't
                # already marked in previous iterations
                #
                yield q
                D[q * q] = [q]
            else:
                # q is composite. D[q] is the list of primes that
                # divide it. Since we've reached q, we no longer
                # need it in the map, but we'll mark the next
                # multiples of its witnesses to prepare for larger
                # numbers
                #
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]

            q += 1


class UnionFind():
    def uf(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while x != self.uf[x]:
            x_root = self.uf[x]
            self.uf[x] = self.uf[x_root]
            x = self.uf[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.uf[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0


# import bisect
# class SolutionSlow:
#     def largestComponentSize(self, A: List[int]) -> int:
#         def compute_gcd(x, y):
#             while(y):
#                 next_x = y
#                 y = x % y
#                 x = next_x
#             return x

#         num_chain = dict()
#         remaining_A = set(A)
#         while remaining_A:
#             changed = True
#             seed = super_lcm = remaining_A.pop()
#             chain = [seed]
#             while changed:

#                 changed = False
#                 next_remaining_A = []

#                 for val in remaining_A:
#                     gdc = compute_gcd(super_lcm, val)
#                     if gdc > 1:
#                         super_lcm = super_lcm * val // gdc
#                         chain.append(val)
#                         changed = True
#                     else:
#                         next_remaining_A.append(val)
#                 remaining_A = next_remaining_A

#             num_chain[seed] = chain

#         # print(num_chain)
#         return len(max(num_chain.values(), key=lambda x: len(x)))


# primes bullshit like always
# import bisect
# class Solution:
#     def largestComponentSize(self, A: List[int]) -> int:


#         primes = set(self.SieveOfEratosthenes(max(A)//2 + 1))
#         # primesDict = {prime : [num for num in A if (not(num % prime))] for prime in primes}
#         numbersWithPrime = dict.fromkeys(primes, [])
#         primesOfNumbers = dict.fromkeys(A, [])
#         minI = 0
#         for prime in primes:
#             minI = bisect.bisect(A, prime, start = minI)
#             primesDict[prime] = [num for num in A[minI:] if (not(num % prime))]
#         print(primesDict)


#         primesChain = dict()
#         while primes:
#             start.primes.pop()


#     # https://www.geeksforgeeks.org/sieve-of-eratosthenes/
#     def SieveOfEratosthenes(self, num : int) -> [int]:
#         primesBool = [True] * (num + 1)
#         primesBool[0] = primesBool[1] = False
#         p = 2
#         while p * p <= num:
#             if (primesBool[p]):
#                 # Update all multiples of p
#                 for i in range(p * p, num + 1, p):
#                     primesBool[i] = False
#             p += 1

#         return (i for i in range(num + 1) if primesBool[i])
