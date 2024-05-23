"""
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an
absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly
none) elements from nums. Two subsets are different if and only if the chosen
indices to delete are different.

Constraints:
- 1 <= nums.length <= 20
- 1 <= nums[i], k <= 1000
"""

from collections import defaultdict


class Solution:

    def beautifulSubsets(self, nums: list[int], k: int) -> int:
        return self.beautifulSubsets_naive(nums, k)

    def beautifulSubsets_naive(self, nums: list[int], k: int) -> int:
        """
        O(2^n) / O(n)       time / space complexity
        """

        def dfs(idx: int) -> int:
            nonlocal occurances
            if idx == len(nums):
                return 1

            taken = 0
            if occurances[nums[idx] - k] == 0:
                occurances[nums[idx]] += 1
                taken = dfs(idx + 1)
                occurances[nums[idx]] -= 1

            notTaken = dfs(idx + 1)

            return taken + notTaken

        nums.sort()
        occurances: defaultdict[int, int] = defaultdict(int)
        ans = dfs(0)
        return ans - 1  # subtract empty set
