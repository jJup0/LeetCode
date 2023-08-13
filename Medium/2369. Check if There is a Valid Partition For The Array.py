class Solution:
    """
    You are given a 0-indexed integer array nums. You have to partition the
    array into one or more contiguous subarrays.

    We call a partition of the array valid if each of the obtained subarrays
    satisfies one of the following conditions:
    - The subarray consists of exactly 2 equal elements.
      For example, the subarray [2,2] is good.
    - The subarray consists of exactly 3 equal elements.
      For example, the subarray [4,4,4] is good.
    - The subarray consists of exactly 3 consecutive increasing elements, that
      is, the difference between adjacent elements is 1.
      For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.

    Return true if the array has at least one valid partition. Otherwise, return false.

    Constraints:
    - 2 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^6
    """

    def validPartition(self, nums: list[int]) -> bool:
        is_valid: list[bool | None] = [None] * (len(nums) + 2)
        is_valid[0] = True

        def helper(subarr_idx: int) -> bool:
            """Returns True if nums[:subarr_idx] can be partitioned, else False"""
            nonlocal is_valid
            if subarr_idx < 0:
                return False

            # check previously calculated result first
            res = is_valid[subarr_idx]
            if res is not None:
                return res

            # need to calculate result

            res = False
            i = subarr_idx - 1
            curr_num = nums[i]
            prev_num = nums[i - 1]
            if curr_num == prev_num:
                if helper(subarr_idx - 2):
                    # curr and previous num are the same, and nums[:subarr_idx-2] can
                    # be partitioned, so nums[:subarr_idx] can be partitioned
                    res = True
                elif curr_num == nums[i - 2]:
                    # idx - 2 may be negative, but then helper(idx-3) will return false
                    if helper(subarr_idx - 3):
                        # the last 3 numbers are equal and nums[:subarr_idx-3] can be partitioned
                        res = True
            else:
                # check if the last three numbers increment in steps
                # of 1, and and nums[:subarr_idx-3] can be partitioned
                one_step_ascending = curr_num == prev_num + 1 == nums[i - 2] + 2
                res = one_step_ascending and helper(subarr_idx - 3)

            # memoize the result and return
            is_valid[subarr_idx] = res
            return res

        return helper(len(nums))


class SolutionCache:
    from functools import cache

    # uses @cache, simpler to write, but in testing twice as slow since dict is used for memoization
    def validPartition(self, nums: list[int]) -> bool:
        self.nums = nums
        res = self._valid_partition(len(nums) - 1)
        print([self._valid_partition(i) for i in range(len(nums))])
        return res

    @cache
    def _valid_partition(self, idx: int) -> bool:
        if idx <= 0:
            return idx == -1

        if self.nums[idx] == self.nums[idx - 1]:
            if self._valid_partition(idx - 2):
                return True

            if self.nums[idx] == self.nums[idx - 2]:
                if self._valid_partition(idx - 3):
                    return True

        ascending = self.nums[idx] == self.nums[idx - 1] + 1 == self.nums[idx - 2] + 2
        return ascending and self._valid_partition(idx - 3)
