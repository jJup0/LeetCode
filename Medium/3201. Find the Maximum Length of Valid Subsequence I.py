"""
You are given an integer array nums.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.

Return the length of the longest valid subsequence of nums.

A subsequence is an array that can be derived from another array by deleting
some or no elements without changing the order of the remaining elements.
"""


class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        """
        For a subsequence to be valid all values must have the same parity or alternating parity.
        Find the maximum of all even, all odd and alternating.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        all_odds = sum(num & 1 for num in nums)
        all_evens = len(nums) - all_odds

        alternating = 0
        next_parity = nums[0] & 1
        for num in nums:
            if num & 1 == next_parity:
                alternating += 1
                next_parity = 1 - next_parity
        return max(all_odds, all_evens, alternating)


def test():
    sol = Solution()
    res = sol.maximumLength([2, 39, 23])
    assert res == 2, res


test()
