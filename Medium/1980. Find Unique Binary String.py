"""
Given an array of strings nums containing n unique binary strings each of
length n, return a binary string of length n that does not appear in nums. If
there are multiple answers, you may return any of them.

Constraints:
- n == nums.length
- 1 <= n <= 16
- nums[i].length == n
- nums[i]  is either'0' or'1'.
- All the strings of nums are unique.
"""


class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        Use diagonalization to find a new number.
        https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument

        Complexity:
            Time: O(n)
            Space: O(n)
        """
        non_existant: list[str] = []
        for i, num in enumerate(nums):
            bit = num[i]
            if bit == "1":
                non_existant.append("0")
            else:
                non_existant.append("1")
        return "".join(non_existant)
