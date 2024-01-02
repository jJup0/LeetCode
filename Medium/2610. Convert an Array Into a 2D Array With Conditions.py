"""
You are given an integer array nums. You need to create a 2D array from nums
satisfying the following conditions:
- The 2D array should contain only the elements of the array nums.
- Each row in the 2D array contains distinct integers.
- The number of rows in the 2D array should be minimal.

Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= nums.length
"""


from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        """
        O(n) / O(n)     time / space complexity
        """
        res: list[list[int]] = []
        for num, count in Counter(nums).items():
            if count >= len(res):
                res.extend([] for _ in range(count - len(res)))
            for i in range(count):
                res[i].append(num)
        return res
