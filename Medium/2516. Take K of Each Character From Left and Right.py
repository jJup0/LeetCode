"""
You are given a string s consisting of the characters'a','b', and'c' and a
non-negative integer k. Each minute, you may take either the leftmost character
of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each
character, or return -1 if it is not possible to take k of each character.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only the letters'a','b', and'c'.
- 0 <= k <= s.length
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        if k == 0:
            return 0
        # find l such that s[:l+1] contains `k` occurances of each letter
        # bind l for typechecker
        l = -1
        # count of a, b and c in s[:l+1]
        char_count = [0, 0, 0]
        ord_a = ord("a")
        for l, char in enumerate(s):
            char_count[ord(char) - ord_a] += 1
            if all(c >= k for c in char_count):
                break
        if not all(c >= k for c in char_count):
            # not enough characters in
            return -1

        # sliding window, take letters from the right and drop
        # letters from left as long as `k` of each letter are
        # still in the counter
        res = l + 1
        for r in range(len(s) - 1, -1, -1):
            char = s[r]
            char_count[ord(char) - ord_a] += 1
            while all(c >= k for c in char_count):
                res = min(res, l + len(s) - r + 1)
                if l < 0:
                    # no more letters from left side to drop
                    return res
                char_count[ord(s[l]) - ord_a] -= 1
                l -= 1
        return res
