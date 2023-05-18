class Solution:
    """
    You are given an array of integers nums and an integer target.

    Return the number of non-empty subsequences of nums such that the sum of the
    minimum and maximum element on it is less or equal to target. Since the answer
    may be too large, return it modulo 10^9 + 7.

    Constraints:
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^6
        1 <= target <= 10^6
    """

    def numSubseq(self, nums: list[int], target: int) -> int:
        res, mod = 0, 1_000_000_007
        powers_of_two = [1]
        for _ in range(1, len(nums) + 1):
            powers_of_two.append((powers_of_two[-1] << 1) % mod)

        # sort number, as only sub sequences are important,
        # so instead go through consecutive sequences of sorted numbers
        nums.sort()

        l = 0
        r = len(nums) - 1
        while l <= r:
            # if sum of smallest and largest are larger than target,
            # then decrease largest number
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                # else, add all possible subsequences, which is just
                # 2 to the power of the length of the current sequence
                res = (res + powers_of_two[r - l]) % mod
                # increase the smallest number
                l += 1

        return res
