"""
You are given a string s consisting only of the characters '0' and '1'. In one
operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal. For
example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to makesalternating.

Constraints:
- 1 <= s.length <= 10^4
- s[i] is either '0' or '1'.
"""


class Solution:
    def minOperations(self, s: str) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        # number of operations need to make string alternating if the first digit is 0
        changes_zero_start = 0
        for i, c in enumerate(s):
            index_is_odd = i & 1
            changes_zero_start += (c == "1") ^ index_is_odd

        changes_one_start = len(s) - changes_zero_start
        return min(changes_zero_start, changes_one_start)
