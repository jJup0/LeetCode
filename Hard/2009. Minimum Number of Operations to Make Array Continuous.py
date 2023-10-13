import bisect


class Solution:
    """
    You are given an integer array nums. In one operation, you can replace any
    element in nums with any integer.

    nums is considered continuous if both of the following conditions are fulfilled:
    - All elements in nums are unique.
    - The difference between the maximum element and the minimum element in nums
      equals nums.length - 1.

    For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

    Return the minimum number of operations to make nums continuous.

    Constraints:
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^9
    """

    def minOperations(self, nums: list[int]) -> int:
        return self.minOperations_bisect(nums)

    def minOperations_bisect(self, nums: list[int]) -> int:
        """
        For a minimum size consecutive sequence, either the first of last number
        must already be in nums.
        Iterate through each number and check cost for if this number is the first
        or last number used in the continuous sequeunce.
        O(n*log(n)) / O(n*log(n))
        """
        # edge case, would otherwise cause runtime error when using bisect
        if len(nums) == 1:
            return 0

        # use unique nums in order to binary search array for start/end number.
        # Duplicates ruin binary search result.
        sorted_unique_nums = sorted(set(nums))

        unique_nums_length = len(sorted_unique_nums)
        original_length = len(nums)
        res = original_length

        for i, num in enumerate(sorted_unique_nums):
            # num as first number
            target_last_number = num + original_length - 1
            r_idx = bisect.bisect(sorted_unique_nums, target_last_number, lo=i)
            # if sorted_unique_nums[r_idx] is the target number, then we can reduce cost by 1
            last_number_included = (
                r_idx < unique_nums_length
                and sorted_unique_nums[r_idx] == target_last_number
            )
            cost_num_is_first = i + (original_length - r_idx) - last_number_included

            # analogously for num as last number
            target_first_number = num - original_length + 1
            l_idx = bisect.bisect(sorted_unique_nums, target_first_number, hi=i)
            first_number_included = sorted_unique_nums[l_idx] == target_first_number
            cost_num_is_last = l_idx + (original_length - i) - first_number_included

            res = min(res, cost_num_is_first, cost_num_is_last)
        return res

    def minOperations_sliding_window(self, nums: list[int]):
        n = res = len(nums)
        unique_sorted_nums = sorted(set(nums))
        i, j = 0, 0
        for i, num in enumerate(unique_sorted_nums):
            while j < len(unique_sorted_nums) and unique_sorted_nums[j] - num < n:
                j += 1
            res = min(res, len(unique_sorted_nums) - (j - i))
        return res

    def minOperations_sliding_window2(self, nums: list[int]) -> int:
        n = len(nums)
        unique_sorted_nums = sorted(set(nums))
        best_consecutive_numbers = i = 0
        for j, num in enumerate(unique_sorted_nums):
            if num - unique_sorted_nums[i] >= n:
                i += 1
            best_consecutive_numbers = max(best_consecutive_numbers, j - i + 1)
        return n - best_consecutive_numbers

    def minOperations_magic(self, nums: list[int]) -> int:
        # just like sliding_window2, but no need to update res every loop
        n = len(nums)
        nums = sorted(set(nums))
        i = j = 0
        for j, num in enumerate(nums):
            # note that we are adding a boolean value here
            i += num - nums[i] >= n
        return (n - 1) - (j - i)
