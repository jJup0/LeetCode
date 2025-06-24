"""
You are given a 0-indexed integer array nums and two integers key and k. A
k-distant index is an index i of nums for which there exists at least one index
j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
- key is an integer from the array nums.
- 1 <= k <= nums.length
"""


class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        res: list[int] = []
        for i, num in enumerate(nums):
            if num != key:
                continue

            # calculate leftmost index to be included that is not already included
            if not res:
                l = max(0, i - k)
            else:
                l = max(res[-1] + 1, i - k)
            # rightmost index to include
            r = min(i + k, len(nums) - 1)

            res.extend(range(l, r + 1))
        return res
