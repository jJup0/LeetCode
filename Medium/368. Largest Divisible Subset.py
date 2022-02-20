from bisect import bisect
from math import sqrt


class Solution:
    def largestDivisibleSubset(self, nums: [int]) -> [int]:

        # they have a cheecky [20000000] testcase, kinda just cheating
        if len(nums) == 1:
            return nums

        nums.sort()
        dp = dict()

        for num in nums:
            # doesnt include factor pairs, only the smaller factor
            factors = [divisor for divisor in range(1, int(sqrt(num)) + 1) if not (num % divisor)]
            largestSubSet = []
            for f in factors:
                if (f in dp) and len(dp[f]) > len(largestSubSet):
                    largestSubSet = dp[f]

                # get factor pair
                f = num // f
                if (f in dp) and len(dp[f]) > len(largestSubSet):
                    largestSubSet = dp[f]

            dp[num] = largestSubSet + [num]

        return max(dp.values(), key=len)


class SolutionOLD:

    def largestDivisibleSubsetPrime(self, nums: [int]) -> [int]:
        # tried to do it with prime factors, too complicated
        nums.sort()
        dp = defaultdict(list)
        primes = self.SieveOfEratosthenes(int(sqrt(nums[-1])) + 1)
        print(primes)

        def getFactor(num):
            numSqrtInt = int(sqrt(num)) + 1

            maxPrimeIdx = bisect(primes, numSqrtInt)

            primesFactors = [divisor for divisor in primes[:maxPrimeIdx + 1] if not (num % divisor)]
            factors = []
            for prime in primeFactors:
                primePower = prime * prime
                while prime < numSqrtInt:
                    if not (num % primePower):
                        factors.append(primePower)
                    primePower *= prime

        for num in nums:
            factors = getFactor(num)
            print(num, factors)
            largest = []
            for f in factors:
                if f in dp and len(dp[f]) > len(largest):
                    largest = dp[f]

                f = num // f
                if f in dp and len(dp[f]) > len(largest):
                    largest = dp[f]
            print(dp)
            print()
            dp[num] = largest + [num]

        return max(dp.values(), key=len)

    # from https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
    def SieveOfEratosthenes(self, n):
        # Create a boolean array "prime[0..n]" and initialize
        # all entries it as true. A value in prime[i] will
        # be false if it is not a prime, else true.
        primesBool_l = [True] * (n + 1)
        primesBool_l[0] = False
        primesBool_l[1] = False
        primes = []
        p = 2
        while (p <= n):

            # If prime[p] has not been sieved, its a prime
            if (primesBool_l[p]):
                primes.append(p)

                # all multiples of p are not prime
                for i in range(p * p, n + 1, p):
                    primesBool_l[i] = False

            p += 1

        return primes

#             [1]
# [1,2,4,8]
# [20000000]

        # def largestDivisibleSubset1(self, nums: [int]) -> [int]:
        # dp = [[]]
        # for n in sorted(nums):
        #     dp.append(max((divSubSet+[n] for divSubSet in dp
        #                    if (divSubSet == []) or n % divSubSet[-1] == 0), key=len))
        #     # n will always be bigger than divSubSet[-1], so check for n % divSubSet[-1] not other way around
        # return max(dp, key=len)
