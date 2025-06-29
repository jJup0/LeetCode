"""
You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the
minimum and maximum element on it is less or equal to target. Since the answer
may be too large, return it modulo 10^9 + 7.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
- 1 <= target <= 10^6
"""


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """Sort + sliding window approach.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        MOD = 10**9 + 7

        # precompute large powers of two
        powers_of_two = [1]
        for _ in range(1, len(nums) + 1):
            powers_of_two.append((powers_of_two[-1] << 1) % MOD)

        # sort number, as only sub sequences are important,
        # so instead go through consecutive sequences of sorted numbers
        nums.sort()

        res = 0
        # left and right pointer of sliding window
        l = 0
        r = len(nums) - 1
        while l <= r:
            # if sum of smallest and largest are larger than target,
            # then decrease largest number
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                # else, add all possible subsequences, which is just
                # 2 to the power of the length of the current sequence - 1
                res = (res + powers_of_two[r - l]) % MOD
                # increase the smallest number
                l += 1

        return res
