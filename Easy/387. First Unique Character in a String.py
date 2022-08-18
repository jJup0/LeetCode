from collections import Counter


class Solution:
    """
    Given a string s, find the first non-repeating character in it and return its index. If it does
    not exist, return -1.
    Constraints:
        1 <= s.length <= 105
        s consists of only lowercase English letters.
    """

    def firstUniqChar(self, s: str) -> int:
        """
        WARNING NEEDS PYTHON 3.7
        make use of the fact that dictionaries (Counters are a subclass of dictionaries) maintain
        insertion order, so to find first single occurance of letter, regular iteration can be used

        O(n) / O(n)     time / space complexity
        """

        for char, count in Counter(s).items():
            if count == 1:
                # once letter with single occurance is found, index it in the word
                return s.index(char)
        return -1

    def firstUniqChar_backwardsCompatible(self, s: str) -> int:
        n = len(s)
        # track occurances of characters in s
        idxs = {}
        for i, c in enumerate(s):
            # if character has previously appeared set last appearance to a constant or greater
            # than n-1 to mark it as a duplicate letter
            if c in idxs:
                idxs[c] = n
            else:
                # else remember index
                idxs[c] = i

        # return smallest index, or -1 if only duplicates
        res = min(idxs.values())
        return -1 if res == n else res
