from collections import defaultdict
from typing import List


class Solution:
    """
    On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may
    have at most one stone.

    A stone can be removed if it shares either the same row or the same column as another stone
    that has not been removed.

    Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith
    stone, return the largest possible number of stones that can be removed.

    Constraints:
        1 <= stones.length <= 1000
        0 <= xi, yi <= 10^4
        No two stones are at the same coordinate point.
    """

    def removeStones(self, stones: List[List[int]]) -> int:
        """
        Basically a graph problem, stones are nodes, and there exists an edge between to stones, if
        they either share a x- or y-coordinate. Find find all trees in the graph, in each tree
        remove leaf nodes until there is only one remaining for optimal removal.
        O(n) / O(n)     time / space complexity
        """

        # union find data structure
        UF = {}

        # unionfind find method, updates parents along the way O(1) amortized time complexity
        def find(x: int) -> int:
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        # unionfind union method, O(1) amortized time complexity
        def union(col: int, row: int) -> None:
            UF.setdefault(col, col)
            UF.setdefault(row, row)
            UF[find(col)] = find(row)

        # treat row and column as separate entities that can be put in a union
        # x and y are guaranteed non negative, so just negate y and subtract one, to make 0
        # unambiguous (-y-1 == ~y)
        for x, y in stones:
            union(x, -y-1)

        # find total number of roots (trees) in the union set, these cannot be removed, so subtract
        # that number from the total stone count for the result
        return len(stones) - len({find(x) for x in UF})
