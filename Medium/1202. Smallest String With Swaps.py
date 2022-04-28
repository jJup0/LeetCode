from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # track "parents" of string indexes, union-find data structure
        parents = list(range(len(s)))

        # define union-find data structure functions
        def union(a, b):
            parents[find(a)] = find(b)

        # O(n) amortized time
        def find(a):
            if parents[a] != a:
                parents[a] = find(parents[a])
            return parents[a]

        # create a union between indexes dependent on pairs
        for a, b in pairs:
            union(a, b)

        # create groups from unions
        groups = defaultdict(lambda: ([], []))
        for i, ch in enumerate(s):
            parent = find(i)
            groups[parent][0].append(i)
            groups[parent][1].append(ch)

        # construct result: each group of indexes can rearrange their
        # characters in alphabetical order and assign it to the result in order of indexes
        res_char_arr = [''] * len(s)
        for idxs, chars in groups.values():
            idxs.sort()
            chars.sort()
            for ch, i in zip(chars, idxs):
                res_char_arr[i] = ch

        # return string representation
        return ''.join(res_char_arr)
