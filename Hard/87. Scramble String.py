from collections import Counter
from functools import cache


class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        """
        Complexity:
            Time: O(n^3)
            Space: O(n^3)
        """
        assert len(s1) == len(s2)
        if s1 == s2:
            return True

        if len(s1) == 1:
            # both are length 1 and not equal
            return False

        # try splitting without swapping
        if self._find_scamble_splits(s1, s2):
            return True
        # splitting and swapping the two substrings in the same as reversing and then spliting
        return self._find_scamble_splits(s1, s2[::-1])

    def _find_scamble_splits(self, s1: str, s2: str) -> bool:
        char_diff: Counter[str] = Counter()
        # try splitting without swapping
        for split_idx, (c1, c2) in enumerate(
            zip(s1[:-1], s2[:-1], strict=True), start=1
        ):
            char_diff[c1] += 1
            char_diff[c2] -= 1
            if char_diff[c1] == 0:
                char_diff.pop(c1)
            if c2 != c1 and char_diff[c2] == 0:
                char_diff.pop(c2)
            if not char_diff:
                if self.isScramble(s1[:split_idx], s2[:split_idx]) and (
                    self.isScramble(s1[split_idx:], s2[split_idx:])
                ):
                    return True
        return False


def test():
    s = Solution()
    res = s.isScramble("great", "rgeat")
    assert res is True, res
    res = s.isScramble("abc", "cba")
    assert res is True, res
    res = s.isScramble("abcdefg", "abcdgef")
    assert res is False, res
    # times out without memoization
    res = s.isScramble("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd")
    assert res is False, res
