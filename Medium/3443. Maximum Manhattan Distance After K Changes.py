"""
You are given a string s consisting of the characters'N','S','E', and'W', where
s[i] indicates movements in an infinite grid:
-'N': Move north by 1 unit.
-'S': Move south by 1 unit.
-'E': Move east by 1 unit.
-'W': Move west by 1 unit.

Initially, you are at the origin (0, 0). You can change at most k characters to
any of the four directions.

Find the maximumManhattan distance from the origin that can be achieved at any
time while performing the movements in order.

The
between two cells
and
is
.
Constraints:
- 1 <= s.length <= 10^5
- 0 <= k <= s.length
- s consists of only'N','S','E', and'W'.
"""

from collections import Counter


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        return self.maxDistance2(s, k)

    def maxDistance1(self, s: str, k: int) -> int:
        """
        Keep track of current steps taken so far. Change as many moves as
        possible that took an opposite direction to current coordinates.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        count = {c: 0 for c in "NSEW"}
        res = 0
        for c in s:
            count[c] += 1
            wrong_dir = manhattan_distance = 0
            for direction1, direction2 in ("NS", "EW"):
                manhattan_distance += abs(count[direction1] - count[direction2])
                wrong_dir += min(count[direction1], count[direction2])
            # flip directions that point in the opposite
            # direction of current coordinates
            manhattan_distance += min(k, wrong_dir) * 2
            res = max(res, manhattan_distance)
        return res

    def maxDistance2(self, s: str, k: int) -> int:
        """
        Same as original implementation, but iterate backwards through s,
        breaking early if result cannot get any bigger.
        Twice as fast in LeetCode test-suite.
        """
        count = Counter(s)
        res = 0
        for i, c in enumerate(reversed(s), start=1):
            wrong_dir = right_dir = 0
            for dir1, dir2 in ("NS", "EW"):
                right_dir += abs(count[dir1] - count[dir2])
                wrong_dir += min(count[dir1], count[dir2])
            right_dir += min(k, wrong_dir) * 2
            res = max(res, right_dir)
            if res > len(s) - i:
                break
            count[c] -= 1
        return res


def test():
    sol = Solution()
    res = sol.maxDistance("NWSE", 1)
    assert res == 3, res
    res = sol.maxDistance("NSWWEW", 3)
    assert res == 6, res


test()
