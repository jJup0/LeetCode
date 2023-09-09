class Solution:
    """
    Given an array of distinct integers nums and a target integer target, return
    the number of possible combinations that add up to target.

    The test cases are generated so that the answer can fit in a 32-bit integer.

    Constraints:
    - 1 <= nums.length <= 200
    - 1 <= nums[i] <= 1000
    - All the elements of nums are unique.
    - 1 <= target <= 1000
    """

    def combinationSum4(self, nums: list[int], target: int) -> int:
        """
        Simply DP solution, adding previous results to current
        O(n * target) / O(target)   time / space complexity
        """

        ways_to_sum = [0] * (target + 1)
        # there is 1 way to make 0: using 0 numbers
        ways_to_sum[0] = 1

        for curr_sum in range(1, target + 1):
            for num in nums:
                prev_sum = curr_sum - num
                if prev_sum >= 0:
                    ways_to_sum[curr_sum] += ways_to_sum[prev_sum]

        return ways_to_sum[target]
