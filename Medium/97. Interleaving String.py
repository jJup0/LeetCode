from functools import cache


class Solution:
    """
    Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of
    s1 and s2.

    An interleaving of two strings s and t is a configuration where they are divided
    into non-empty substrings such that:
    - s = s1 + s2 + ... + sn
    - t = t1 + t2 + ... + tm
    - |n - m| <= 1
    - The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or
      t1 + s1 + t2 + s2 + t3 + s3 + ...
    - Note: a + b is the concatenation of strings a and b

    Constraints:
    - 0 <= s1.length, s2.length <= 100
    - 0 <= s3.length <= 200
    - s1, s2, and s3 consist of lowercase English letters.
    """

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def is_interleave_(i1: int, i3: int):
            """
            Returns True if and only if s3[:i3+1] is an interleaving of s1[:i1+1] and s2[:i3-i1]
            """
            if i3 == -1:
                # if i3 == -1, then i3 == 0 must have recusively called because a character matched, so return True
                return True
            char_to_match = s3[i3]

            if i1 >= 0 and s1[i1] == char_to_match:
                # if char in s1 matches, recursivly call, return True if True
                if is_interleave_(i1 - 1, i3 - 1):
                    return True

            i2 = i3 - i1 - 1
            if i2 >= 0 and s2[i2] == char_to_match:
                # if char in s2 matches, recursivly call, return True if True
                if is_interleave_(i1, i3 - 1):
                    return True

            # neither the char in s1 nor s2 match
            return False

        if len(s1) + len(s2) != len(s3):
            # if lengths do not match up return false
            return False
        return is_interleave_(len(s1) - 1, len(s3) - 1)
