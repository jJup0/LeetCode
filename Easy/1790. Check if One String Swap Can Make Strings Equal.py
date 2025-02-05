"""
You are given two strings s1 and s2 of equal length. A string swap is an
operation where you choose two indices in a string (not necessarily different)
and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most
one string swap on exactly one of the strings. Otherwise, return false.

Constraints:
- 1 <= s1.length, s2.length <= 100
- s1.length == s2.length
- s1 and s2 consist of only lowercase English letters.
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        # character mismatches in s1 and s2
        bad_in_s1: list[str] = []
        bad_in_s2: list[str] = []
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            bad_in_s1.append(c1)
            bad_in_s2.append(c2)
            if len(bad_in_s1) == 3:
                # would need at least 2 swaps
                return False

        # return true iff the characters can be swapped
        return bad_in_s1 == bad_in_s2[::-1]
