"""
You are given a 0-indexed integer array nums of length n.

You can perform the following operation as many times as you want:
- Pick an index i that you haven't picked before, and pick a prime p strictly
  less than nums[i], then subtract p from nums[i].

Return true if you can make nums a strictly increasing array using the above
operation and false otherwise.

A strictly increasing array is an array whose each element is strictly greater
than its preceding element.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- nums.length == n
"""

import bisect


class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
        """
        Iterate in reverse order, trying to make the largest
        possible number smaller than the previous number.
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        # generate all primes until 1009
        primes = self._get_primes(1010)
        # previous number, initialized with dummy large number
        prev = nums[-1] + 1
        for num in reversed(nums):
            if num < prev:
                # number is larger than previous, no need to subtract
                prev = num
                continue
            # bisect to find best prime to subtract from current number to make it smaller than previous
            prime_sub_idx = bisect.bisect_left(primes, num - prev + 1)
            prime = primes[prime_sub_idx]
            if prime < num:
                # found good prime candidate
                prev = num - prime
            else:
                # best prime candidate is not strictly smaller, no
                # possible prime to make array strictly increasing
                return False
        return True

    def _get_primes(self, max_val: int) -> list[int]:
        # Sieve of Eratosthenes to generate primes
        is_prime = [False, True] * (max_val // 2 + 1)
        primes = [2]
        for i in range(3, max_val + 1, 2):
            if not is_prime[i]:
                continue
            primes.append(i)
            for j in range(i * i, max_val + 1, i):
                is_prime[j] = False
        return primes
