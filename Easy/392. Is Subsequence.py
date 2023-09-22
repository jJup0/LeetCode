class Solution:
    """
    Given two strings s and t, return true if s is a subsequence of t, or
    false otherwise.

    A subsequence of a string is a new string that is formed from the original
    string by deleting some (can be none) of the characters without disturbing
    the relative positions of the remaining characters. (i.e., "ace" is a
    subsequence of "abcde" while "aec" is not).

    Constraints:
    - 0 <= s.length <= 100
    - 0 <= t.length <= 10^4
    - s and t consist only of lowercase English letters.
    """

    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        cur_s_idx = 0
        for tc in t:
            if tc == s[cur_s_idx]:
                cur_s_idx += 1
                if cur_s_idx == len(s):
                    return True
        return False
