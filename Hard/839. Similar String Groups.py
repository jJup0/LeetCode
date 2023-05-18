class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))

    def find(self, x: int) -> int:
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        px = self.find(x)
        py = self.find(y)
        self.parents[px] = py


class Solution:
    """
    Two strings, X and Y, are considered similar if either they are identical or we
    can make them equivalent by swapping at most two letters (in distinct positions)
    within the string X.

    For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and
    "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or
    "arts".

    Together, these form two connected groups by similarity: {"tars", "rats", "arts"}
    and {"star"}.  Notice that "tars" and "arts" are in the same group even though
    they are not similar.  Formally, each group is such that a word is in the group
    if and only if it is similar to at least one other word in the group.

    We are given a list strs of strings where every string in strs is an anagram of
    every other string in strs. How many groups are there?

    Constraints:
        1 <= strs.length <= 300
        1 <= strs[i].length <= 300
        strs[i] consists of lowercase letters only.
        All words in strs have the same length and are anagrams of each other.
    """

    def numSimilarGroups(self, strs: list[str]) -> int:
        """Union find data structure.
        O(n * log(n)) / O(n)    time / space complexity
        """

        def strings_are_similar(str1: str, str2: str) -> bool:
            diff_count = 0
            for c1, c2 in zip(str1, str2):
                if c1 != c2:
                    diff_count += 1
                    # if 3 characters are different strings cannot be similar
                    if diff_count == 3:
                        return False
            # since strings are anagrams, diff between
            # strings is either 0 or greater equal 2:
            # assert diff_count == 0 or diff_count == 2
            return True

        # union find where index of string represents object in union find data structure
        UF = UnionFind(len(strs))

        for i, str1 in enumerate(strs):
            for j in range(i + 1, len(strs)):
                str2 = strs[j]
                # if strings are similar, union between strings
                if strings_are_similar(str1, str2):
                    UF.union(i, j)

        # find all disjoint sets' parents
        parents_set = set(UF.find(i) for i in range(len(strs)))
        return len(parents_set)
