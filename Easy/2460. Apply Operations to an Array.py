"""
You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation
(0-indexed), you will apply the following on the ith element of nums:
- If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to
  0. Otherwise, you skip this operation.

After performing all the operations, shift all the 0's to the end of the array.
- For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end,
  is [1,2,1,0,0,0].

Return the resulting array.

Note that the operations are applied sequentially, not all at once.

Constraints:
- 2 <= nums.length <= 2000
- 0 <= nums[i] <= 1000
"""


class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        """
        Complexity:
            Time: O(n)
            Extra space: O(1)
        """
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        next_pos = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i] = 0
                nums[next_pos] = num
                next_pos += 1
        return nums
