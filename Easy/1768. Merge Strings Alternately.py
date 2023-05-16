class Solution:
    """
    You are given two strings word1 and word2. Merge the strings by adding letters
    in alternating order, starting with word1. If a string is longer than the other,
    append the additional letters onto the end of the merged string.

    Return the merged string.

    Constraints:
        1 <= word1.length, word2.length <= 100
        word1 and word2 consist of lowercase English letters.
    """

    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = []
        for c1, c2 in zip(word1, word2):
            l.append(c1)
            l.append(c2)

        if len(word1) > len(word2):
            l.append(word1[len(word2) :])
        elif len(word1) < len(word2):
            l.append(word2[len(word1) :])
        return "".join(l)
