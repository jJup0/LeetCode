"""
You are given an integer array nums of size n and a positive integer k.

Divide the array into one or more arrays of size 3 satisfying the following
conditions:
- Each element of nums should be in exactly one array.
- The difference between any two elements in one array is less than or equal to
k.

Return a 2D array containing all the arrays. If it is impossible to satisfy the
conditions, return an empty array. And if there are multiple answers, return
any of them.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- n is a multiple of 3.
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^5
"""


class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        """
        Simply sort the array, then check difference of first and last value of each triplet.
        O(n) / O(n)     time / space complexity
        """
        nums.sort()
        res: list[list[int]] = []
        for i in range(0, len(nums), 3):
            a, _b, c = nums_slice = nums[i : i + 3]
            if c - a > k:
                return []
            res.append(nums_slice)
        return res
