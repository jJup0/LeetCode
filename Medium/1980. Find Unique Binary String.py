class Solution:
    """
    Given an array of strings nums containing n unique binary strings each of
    length n, return a binary string of length n that does not appear in nums.
    If there are multiple answers, you may return any of them.

    Constraints:
    - n == nums.length
    - 1 <= n <= 16
    - nums[i].length == n
    - nums[i] is either '0' or '1'.
    - All the strings of nums are unique.
    """

    def findDifferentBinaryString(self, nums: list[str]) -> str:
        """
        Use diagonalization to find a new number.
        https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument
        O(n) / O(n)     time / space complexity
        """
        res_char_list: list[str] = []
        for i, num in enumerate(nums):
            char = num[i]
            if char == "0":
                res_char_list.append("1")
            else:
                res_char_list.append("0")
        return "".join(res_char_list)
