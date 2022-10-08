from typing import List


class Solution:
    """
    Given an integer array nums of length n and an integer target, find three integers in nums such
    that the sum is closest to target.
    Return the sum of the three integers.
    You may assume that each input would have exactly one solution.

    Constraints:
        3 <= nums.length <= 1000
        -1000 <= nums[i] <= 1000
        -10^4 <= target <= 10^4
    """

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        N = len(nums)
        LARGEST = nums[-1] + nums[-2]

        self.res = -1
        self.res_diff = 100_000

        def update_res(diff, candidate):
            if diff < self.res_diff:
                self.res_diff = diff
                self.res = candidate

        for i in range(N - 2):
            curr_num = nums[i]

            # if largest sum possible including nums[i] is smaller than target, update res
            triple_sum = curr_num + LARGEST
            if triple_sum <= target:
                update_res(target - triple_sum, triple_sum)
                continue

            # check if sum(nums[i:i+2]) is bigger than target, if yes update res and break
            # since there can be no smaller sum
            triple_sum = curr_num + nums[i+1] + nums[i+2]
            if triple_sum >= target:
                update_res(triple_sum - target, triple_sum)
                break

            # zero in from both sides to get closer to target
            l = i + 1
            r = N - 1
            while l < r:
                triple_sum = curr_num + nums[l] + nums[r]
                if triple_sum < target:
                    # if sum is too small, take a bigger number for triple sum
                    l += 1
                elif triple_sum > target:
                    # if sum is too big, take a smaller number for triple sum
                    r -= 1
                else:
                    # if target reached, return
                    return triple_sum

            update_res(abs(triple_sum - target), triple_sum)

        return self.res
