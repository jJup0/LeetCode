from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        """
        O(min(n, m)) / O(1)     time / space complexity
        """
        # create generators for every letter in string1 and string2
        gen_string1 = (c for s in word1 for c in s)
        gen_string2 = (c for s in word2 for c in s)

        # compare each letter of the two generators, one cannot use zip, because if string1 has one
        # extra letter, zip will call next() on both gen1 and gen2, consuming the next letter of
        # gen1, but will break on the StopIteration of gen2, so when compared for exhaustion true
        # is returned. Example: word1 = ["ab"], word2 = ["a"]
        string2_starts_with_string1 = all(c1 == next(gen_string2, None) for c1 in gen_string1)

        # check if gen2 is also exhausted
        return string2_starts_with_string1 and (next(gen_string2, None) == None)

    def arrayStringsAreEqual_oneline(self, word1: List[str], word2: List[str]) -> bool:
        """
        O(n + m) / O(n + m)     time / space complexity
        """
        return ''.join(word1) == ''.join(word2)
