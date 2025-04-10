"""
You are given an integer array nums and an integer k.

An integer h is called valid if all values in the array that are strictly
greater than h are identical.

For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all
nums[i] > 9 are equal to 10, but 5 is not a valid integer.

You are allowed to perform the following operation on nums:
- Select an integer h that is valid for the current values in nums.
- For each index i where nums[i] > h, set nums[i] to h.

Return the minimum number of operations required to make every element in nums
equal to k. If it is impossible to make all elements equal to k, return -1.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
- 1 <= k <= 100
"""


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        """
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        sorted_nums = sorted(set(nums))
        if sorted_nums[0] < k:
            return -1
        if sorted_nums[0] == k:
            return len(sorted_nums) - 1
        return len(sorted_nums)
        k = 0
        res = 0
        for num in sorted_nums:
            if num >= k:
                break
            res += 1
        return res
