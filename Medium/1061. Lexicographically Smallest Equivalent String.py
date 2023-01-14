class UF:
    def __init__(self, parents_init):
        self.parents = parents_init

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        # ensure that parent of larger letter is always smaller letter
        if a < b:
            self.parents[b] = a
        else:
            self.parents[a] = b

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    """
    You are given two strings of the same length s1 and s2 and a string baseStr.

    We say s1[i] and s2[i] are equivalent characters.

    For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
    Equivalent characters follow the usual rules of any equivalence relation:

    Reflexivity: 'a' == 'a'.
    Symmetry: 'a' == 'b' implies 'b' == 'a'.
    Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
    For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and
    "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest
    equivalent string of baseStr.

    Return the lexicographically smallest equivalent string of baseStr by using the equivalency
    information from s1 and s2.

    Constraints:
        1 <= s1.length, s2.length, baseStr <= 1000
        s1.length == s2.length
        s1, s2, and baseStr consist of lowercase English letters.
    """

    def smallestEquivalentString(self, s1: str, s2: str, base_str: str) -> str:
        """
        O(n) / O(n)     time / space complexity
        """
        # Simple union find problem. Find smallest equivalent character for
        # each character and then simply replace letters in baseStr for result

        alph_iter = (chr(x) for x in range(ord('a'), ord('z') + 1))
        uf = UF({c: c for c in alph_iter})

        for a, b in zip(s1, s2):
            uf.union(b, a)

        return ''.join(uf.find(c) for c in base_str)
