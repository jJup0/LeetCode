"""
Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        return self.firstUniqChar_python_37(s)

    def firstUniqChar_python_37(self, s: str) -> int:
        """
        Make use of the fact that dictionaries (Counters are a subclass of dictionaries) maintain
        insertion order since python 3.7.
        O(n) / O(n)     time / space complexity
        """

        for char, count in Counter(s).items():
            if count == 1:
                # once letter with single occurance is found, index it in the word
                return s.index(char)
        return -1

    def firstUniqChar_backwardsCompatible(self, s: str) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        DUPLICATE_LETTER = len(s)
        # track occurances of characters in s
        idxs: dict[str, int] = {}
        for i, c in enumerate(s):
            # if character has previously appeared set last appearance to a constant or greater
            # than n-1 to mark it as a duplicate letter
            if c in idxs:
                idxs[c] = DUPLICATE_LETTER
            else:
                # else remember index
                idxs[c] = i

        # return smallest index, or -1 if only duplicates
        res = min(idxs.values())
        if res == DUPLICATE_LETTER:
            return -1

        return res
