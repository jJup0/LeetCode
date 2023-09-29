class Solution:
    """
    An array is monotonic if it is either monotone increasing or monotone
    decreasing.

    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
    An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

    Given an integer array nums, return true if the given array is monotonic,
    or false otherwise.

    Constraints:
    - 1 <= nums.length <= 10^5
    - -10^5 <= nums[i] <= 10^5
    """

    def isMonotonic(self, nums: list[int]) -> bool:
        """
        O(n) / O(1)     time / space complexity
        """
        num = first_num = nums[0]
        i = 0
        for i, num in enumerate(nums):
            if num != first_num:
                break

        if num < first_num:
            return self._is_decreasing(i, nums)
        else:
            return self._is_increasing(i, nums)

    def _is_decreasing(self, starting_i: int, nums: list[int]) -> bool:
        prev_num = nums[starting_i]
        for i in range(starting_i + 1, len(nums)):
            curr_num = nums[i]
            if curr_num > prev_num:
                return False
            prev_num = curr_num
        return True

    def _is_increasing(self, starting_i: int, nums: list[int]) -> bool:
        prev_num = nums[starting_i]
        for i in range(starting_i + 1, len(nums)):
            curr_num = nums[i]
            if curr_num < prev_num:
                return False
            prev_num = curr_num
        return True

    def isMonotonic_alternate(self, nums: list[int]) -> bool:
        prev_num = nums[0]
        desc = False
        incr = False
        for num in nums:
            if num < prev_num:
                desc = True
            elif num > prev_num:
                incr = True

            if incr and desc:
                return False
            prev_num = num
        return True
