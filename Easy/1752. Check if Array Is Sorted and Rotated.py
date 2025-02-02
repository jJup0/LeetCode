"""
Given an array nums, return true if the array was originally sorted in
non-decreasing order, then rotated some number of positions (including zero).
Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same
length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""


class Solution:
    def check(self, nums: list[int]) -> bool:
        """
        Starting with `prev`=nums[-1] iterate through the array and return
        True iff there is at most one sorting violation.
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        prev = nums[-1]
        sorted_violated = False
        for num in nums:
            if num < prev:
                if sorted_violated:
                    return False
                sorted_violated = True
            prev = num
        return True
