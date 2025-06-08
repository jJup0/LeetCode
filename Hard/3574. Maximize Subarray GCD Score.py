"""
You are given an array of positive integers nums and an integer k.

You may perform at most k operations. In each operation, you can choose one
element in the array and double its value. Each element can be doubled at most once.

The score of a contiguous subarray is defined as the product of its length and
the greatest common divisor (GCD) of all its elements.

Your task is to return the maximumscore that can be achieved by selecting a
contiguous subarray from the modified array.

Note:
- A subarray is a contiguous sequence of elements within an array.
- The greatest common divisor (GCD) of an array is the largest integer that
  evenly divides all the array elements.

Constraints:
- 1 <= n == nums.length <= 1500
- 1 <= nums[i] <= 10^9
- 1 <= k <= n
"""

import math
import random
from collections import Counter
from functools import cache

MOD = 10**9 + 7


class Solution1:
    def maxGCDScore(self, nums: list[int], k: int) -> int:
        self.primes = self.generate_primes(int(max(nums) ** 0.5) + 2)
        self.nums = nums
        self.k = k
        self.nums_pfs: list[Counter[int]] = [
            self.get_prime_factors(num) for num in nums
        ]
        res = max(nums) * 2
        for i in range(len(nums)):
            # print(f"loop {i=}")
            for j in range(i + 1, len(nums) + 1):
                res = max(res, self.get_gcd_score(i, j))
        return res

    @cache
    def get_gcd_counter(self, i: int, j: int) -> Counter[int]:
        if i >= j:
            return Counter()
        if i + 1 == j:
            return self.nums_pfs[i].copy()

        mid = (i + j) // 2
        l = self.get_gcd_counter(i, mid)
        r = self.get_gcd_counter(mid, j)
        return l & r

    @cache
    def get_gcd_num(self, i: int, j: int) -> int:
        if i >= j:
            return 1
        if i + 1 == j:
            return sum(f * c for f, c in self.nums_pfs[i].items())

        mid = (i + j) // 2
        l = self.get_gcd_num(i, mid)
        r = self.get_gcd_num(mid, j)
        return math.gcd(l, r)

    @cache
    def smallest_2(self, i: int, j: int) -> int:
        if i >= j:
            return 0
        if i + 1 == j:
            return self.nums_pfs[i][2]
        # return self.smallest_2(i, j - 1) + self.nums_pfs[j - 1][2]
        mid = (i + j) // 2
        l = self.smallest_2(i, mid)
        r = self.smallest_2(mid, j)
        return min(l, r)

    @cache
    def un(self, i: int, j: int, f2: int) -> int:
        if i >= j:
            return 0
        if i + 1 == j:
            return self.nums_pfs[i][2] < f2
        mid = (i + j) // 2
        l = self.un(i, mid, f2)
        r = self.un(mid, j, f2)
        return l + r

    def get_gcd_score(self, i: int, j: int):
        min_2 = m2og = self.smallest_2(i, j)
        if self.un(i, j, min_2):
            min_2 += 1

        length = j - i
        # and_all[2] = min_2
        # gcd = sum(fac * count for fac, count in and_all.items())
        gcd = self.get_gcd_num(i, j)
        gcd //= 1 << m2og
        gcd *= 1 << min_2
        # print(f"{i=} {j=} {gcd=} {length=}")
        return length * gcd

    def get_prime_factors(self, num: int) -> Counter[int]:
        pfs: Counter[int] = Counter()
        for prime in self.primes:
            while num > 1 and num % prime == 0:
                pfs[prime] += 1
                num //= prime
            if num == 1:
                break
        if not pfs:
            pfs[num] = 1
        return pfs

    def generate_primes(self, n: int) -> list[int]:
        if n < 2:
            return []
        is_prime = [False, True] * ((n // 2) + 1)
        primes = [2]
        for i in range(3, n + 1, 2):
            if not is_prime[i]:
                continue
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
        return primes


class Solution2:
    def maxGCDScore(self, nums: list[int], k: int) -> int:
        """
        Complexity:
            Time: O(n^2 * O(math.gcd))
            Space: O(n)
        """
        # for each number, calculate how many times it is divisible by 2
        divisibilty_by_2: list[int] = []
        for num in nums:
            f2 = 0
            while not num & 1:
                num >>= 1
                f2 += 1
            divisibilty_by_2.append(f2)

        res = max(nums) * 2
        for i in range(len(nums)):
            smallest_power_2 = divisibilty_by_2[i]
            # amount of numbers in nums[i:j+1] which have `smallest_power_2`
            # as their divisibility by 2
            smallest_power_2_count = 1
            # current gcd of nums[i:j+1] excluding powers of 2
            curr_gcd = nums[i] // (1 << divisibilty_by_2[i])
            for j in range(i + 1, len(nums)):
                # update smallest factor
                curr_power_2 = divisibilty_by_2[j]
                if curr_power_2 < smallest_power_2:
                    smallest_power_2 = curr_power_2
                    smallest_power_2_count = 1
                elif curr_power_2 == smallest_power_2:
                    smallest_power_2_count += 1
                # if we can multiply all the numbers with the smallest power of 2
                # by two, then increment the smallest power of 2 for this round
                upgraded_2 = smallest_power_2 + (smallest_power_2_count <= k)

                # add current number to gcd
                curr_gcd = math.gcd(curr_gcd, nums[j])

                # gcd score of nums[i:j+1]
                score = curr_gcd * (1 << upgraded_2) * (j - i + 1)

                # update result (note that if check resulted in
                # half the execution time as using max())
                if score > res:
                    res = score
        return res


class Solution(Solution2):
    pass


def test():
    s = Solution()
    res = s.maxGCDScore([2, 4], 1)
    real = 8
    assert res == real, res

    res = s.maxGCDScore([3, 5, 7], 2)
    real = 14
    assert res == real, res

    res = s.maxGCDScore([5, 5, 5], 1)
    assert res == 15, res


def big_test():
    arr = [random.randint(1, 10**9) for _ in range(1500)]
    Solution2().maxGCDScore(arr, 40)


import cProfile

# cProfile.run("big_test()", sort="tottime")
test()
