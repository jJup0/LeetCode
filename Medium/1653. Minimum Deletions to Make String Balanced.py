"""
You are given a string s consisting only of characters'a' and'b'.

You can delete any number of characters in s to make s balanced. s is balanced
if there is no pair of indices (i,j) such that i < j and s[i] ='b' and s[j]='a'.

Return the minimum number of deletions needed to make s balanced.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is'a' or'b'.
"""

from collections import deque


class Solution:
    def minimumDeletions(self, s: str) -> int:
        return self.minmum_deletion_constant_space(s)

    def minimum_linear_space(self, s: str) -> int:
        """
        Calculate prefix sums of a's and reverse prefix sums of b's.
        Iterate over all indices in s, making them the "pivot" from which
        point onwards no more a's are allowed, return minimum removals needed.
        O(n) / O(n)     time / space complexity
        """
        a_count_right: deque[int] = deque()
        a_count = 0
        for c in reversed(s):
            a_count_right.appendleft(a_count)
            a_count += c == "a"

        b_count_left: list[int] = []
        b_count = 0
        for c in s:
            b_count_left.append(b_count)
            b_count += c == "b"

        return min(ar + bl for ar, bl in zip(a_count_right, b_count_left))

    def minmum_deletion_constant_space(self, s: str) -> int:
        """
        When "a" is encountered and a previous, undeleted "b" has been encountered,
        increment result to lazily delete, no need to choose. In the end, the result
        will contain all "unbalanced" pairs of "a" and "b", for each pair only one
        character has to be deleted to balance the string.
        O(n) / O(1)     time / space complexity
        """
        res = 0
        b_count = 0
        for c in s:
            if c == "b":
                b_count += 1
            elif b_count:
                res += 1
                b_count -= 1
        return res
