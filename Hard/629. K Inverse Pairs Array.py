"""
For an integer array nums, an inverse pair is a pair of integers [i, j] where
0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of
numbers from 1 to n such that there are exactly k inverse pairs. Since the
answer can be huge, return it modulo10^9 + 7.

Constraints:
- 1 <= n <= 1000
- 0 <= k <= 1000
"""


from functools import cache
from itertools import permutations

MOD = 10**9 + 7


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        return self.kInversePairs_math(n, k)

    @cache
    def kInversePairs_n_power_3(self, n: int, k: int) -> int:
        """
        Use dynamic programming to store solutions of subproblems.
        Place last number anywhere in the permutation, can permute the rest recursively.
        O(n*k*k) / O(n*k)   time / space complexity
        """
        if not n:
            return int(k == 0)
        if not k:
            return 1
        res = 0
        for idx_for_last in range(max(0, n - k - 1), n):
            # place last element as `idx_for_last`th element
            # this causes `inverses` inverse pairs with all numbers to the right of it
            inverses = n - idx_for_last - 1
            k_remaining = k - inverses
            # we can now permute n-1 numbers freely, without changing
            # the fact that `n` causes `inverses` inverse pairs
            # simply add up all ways to get k_remaining inverse pairs for permutations of [1..n-1]
            res = (res + self.kInversePairs(n - 1, k_remaining)) % MOD
        return res

    @cache
    def kInversePairs_math(self, n: int, k: int) -> int:
        """
        As a baseline algorithm, use n*k^2 method in kInversePairs_n_power_3().
        Base cases are the same.

        Setup up the following equations.

        A := f(n,k)   = f(n-1,k) +  f(n-1,k-1) + f(n-1,k-2) + ... + f(n-1,k-n+1)
        B := f(n,k-1) =             f(n-1,k-1) + f(n-1,k-2) + ... + f(n-1,k-n+1) + f(n-1,k-n)

        A - B = f(n,k) - f(n,k-1) = f(n-1,k) - f(n-1,k-n)
        rearrange to:
        f(n,k) = f(n,k-1) + f(n-1,k) - f(n-1,k-n)
        Now we have a contstant length recursive formula!
        """
        if k == 0:
            return 1
        if k < 0 or n <= 0:
            return 0
        return (
            self.kInversePairs_math(n - 1, k)
            + self.kInversePairs_math(n, k - 1)
            - self.kInversePairs_math(n - 1, k - n)
        ) % MOD

    def kInversePairs_brute_force(self, n: int, k: int) -> int:
        """
        Brute force method used to check implementations.
        x := space complexity of `permutations(n)`
        O(n!) / O(n + x))    time / space complexity
        """
        all_perms = permutations(range(1, n + 1))
        res = 0
        for perm in all_perms:
            inverses = 0
            prevs: list[int] = []
            for val in perm:
                inverses += sum(1 for prev in prevs if prev > val)
                prevs.append(val)

            res += inverses == k
        return res
