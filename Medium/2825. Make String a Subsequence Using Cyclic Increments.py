"""
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in
the set, increment str1[i] to the next character cyclically. That is'a'
becomes'b','b' becomes'c', and so on, and'z' becomes'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing
the operation at most once, and false otherwise.

Note: A subsequence of a string is a new string that is formed from the
original string by deleting some (possibly none) of the characters without
disturbing the relative positions of the remaining characters.

Constraints:
- 1 <= str1.length <= 10^5
- 1 <= str2.length <= 10^5
- str1 and str2 consist of only lowercase English letters.
"""


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        iter_str1 = iter(str1)
        char1 = next(iter_str1)
        for char2 in str2:
            # find next matching character in str1
            # which equals or is one less than char2
            while (
                (char1 != char2)
                and (ord(char1) != ord(char2) - 1)
                and not (char1 == "z" and char2 == "a")
            ):
                char1 = next(iter_str1, None)
                if char1 is None:
                    # str1 exhausted, str2 can not be made into modified
                    # version of str1
                    return False
            # go to next letter in str1, default to character not in charset
            char1 = next(iter_str1, "$")
        return True