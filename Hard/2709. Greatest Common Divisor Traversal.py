"""
You are given a 0-indexed integer array nums, and you are allowed to traverse
between its indices. You can traverse between index i and index j, i != j, if
and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common
divisor.

Your task is to determine if for every pair of indices i and j in nums, where i
< j, there exists a sequence of traversals that can take us from i to j.

Return true if it is possible to traverse between all such pairs of indices, or
false otherwise.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

import math
from collections import defaultdict


class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        return self.canTraverseAllPairs_original(nums)

    def canTraverseAllPairs_original(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            # edge case of edge case, if len(nums) == 1, then 1 is allowed to be in nums
            return True
        if 1 in nums:
            # 1 can never have gcd higher than 1 with any number
            return False

        nums = list(set(nums))
        self.primes: list[int] = self._get_primes(nums)
        self.primes_set = set(self.primes)

        idx_to_prime_factors = [self._get_prime_factors(num) for num in nums]
        print(idx_to_prime_factors)
        return self._all_numbers_reachable(nums, idx_to_prime_factors)

    def _all_numbers_reachable(
        self,
        nums: list[int],
        idx_to_prime_factors: list[set[int]],
    ) -> bool:
        """
        Using calculated prime factors determine if all numbers are reachable.
        O(total factors of all numbers) / O(len(nums))  time / space complexity
        """
        prime_factor_to_idx: defaultdict[int, set[int]] = defaultdict(set)

        for i, factors in enumerate(idx_to_prime_factors):
            for factor in factors:
                prime_factor_to_idx[factor].add(i)

        can_reach = [False] * len(nums)
        can_reach[0] = True
        reachable = [0]
        while reachable:
            idx = reachable.pop()
            can_reach[idx] = True
            for factor in idx_to_prime_factors[idx]:
                if factor not in prime_factor_to_idx:
                    continue
                for factor_neighbor_idx in prime_factor_to_idx[factor]:
                    if can_reach[factor_neighbor_idx]:
                        # already visited
                        continue
                    can_reach[factor_neighbor_idx] = True
                    reachable.append(factor_neighbor_idx)
                prime_factor_to_idx.pop(factor)
        return all(can_reach)

    def _get_prime_factors(self, number: int) -> set[int]:
        factors: set[int] = set()
        for prime in self.primes:
            if prime * prime > number:
                break
            while number % prime == 0:
                factors.add(prime)
                number //= prime
        if number > 1:
            factors.add(number)
        return factors

    def _get_primes(self, nums: list[int]) -> list[int]:
        max_num = max(nums)
        max_sqrt = int(max_num**0.5) + 1
        is_prime = [False, True] * (max_sqrt // 2)
        primes: list[int] = [2]
        for num in range(3, max_sqrt, 2):
            if not is_prime[num]:
                continue
            primes.append(num)
            for multiple in range(num * 3, len(is_prime), num * 2):
                is_prime[multiple] = False
        return primes

    def canTraverseAllPairs_elegant(self, nums: list[int]) -> bool:
        """
        Stolen from fellow leetcoder.
        O(n^2) / O(n)   time / space complexity
        """
        # duplicate numbers do not interest us
        nums_set = set(nums)
        # 1 can never have gcd greater than 1
        if len(nums) > 1 and 1 in nums_set:
            return False
        unique_nums_count = len(nums_set)
        if unique_nums_count == 1:
            return True

        # sort nums to only compare a number to small numbers
        nums = sorted(nums_set, reverse=True)
        for i in range(unique_nums_count - 1):
            found_partner = False
            for j in range(i + 1, unique_nums_count):
                if math.gcd(nums[i], nums[j]) > 1:
                    # create virtual link between nums[i] and nums[j] by multiplying,
                    # effectively "sharing" factors
                    nums[j] *= nums[i]
                    found_partner = True
                    break
            if not found_partner:
                # no gcd greater than one with any smaller number
                return False
        return True
