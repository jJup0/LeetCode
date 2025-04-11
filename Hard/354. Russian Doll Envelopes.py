"""
You are given a 2D array of integers envelopes where envelopes[i] = [w_i, h_i]
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of
one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one
inside the other).

Note: You cannot rotate an envelope.

Constraints:
- 1 <= envelopes.length <= 10^5
- envelopes[i].length == 2
- 1 <= w_i, h_i <= 10^5
"""

import bisect

from sortedcontainers.sortedlist import SortedList


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """Order envelopes by width and track shortest height for each russain depth.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        # sort by width increasing, then height decreasing, as values need
        # to be strictly greater than, this way we avoid placing envelopes
        # of equal width within each other
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # dp[i] = shortest envelope that can have a russain doll depth of i
        dp: list[int] = [0]
        for _w, h in envelopes:
            if h > dp[-1]:
                # widest and tallest envelope so far, can have
                # previous deepest russain envelope inside it
                dp.append(h)
            else:
                # find tallest envelope shorter than current and update the
                # shortest height, an update dp for that depth, guranteed
                # to be shorter, since we order descending
                deepest_compatible = bisect.bisect_left(dp, h)
                dp[deepest_compatible] = h

        return len(dp) - 1


class Solution1:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        """Original solution, over complicated, assumed that removal from sorted list needed.

        Assertions added after the fact show this.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        # (height, depth)
        russain_stacks = SortedList([(0, 0)])
        for _w, h in envelopes:
            compatible_idx = russain_stacks.bisect((h - 1, 1_000_000)) - 1
            compatible_depth: int = russain_stacks[compatible_idx][1]

            if compatible_idx == len(russain_stacks) - 1:
                # new heighest envelope, add to sorted list
                russain_stacks.add((h, compatible_depth + 1))
                continue

            if russain_stacks[compatible_idx + 1][0] <= h:
                # for same depth a shorter envelope already exists
                continue

            pop_count = 0
            while compatible_idx + 1 < len(russain_stacks):
                _prev_height, prev_depth = russain_stacks[compatible_idx + 1]
                if prev_depth <= compatible_depth + 1:
                    pop_count += 1
                    assert prev_depth == compatible_depth + 1
                    russain_stacks.pop(compatible_idx + 1)
                else:
                    break
            assert pop_count == 1
            russain_stacks.add((h, compatible_depth + 1))

        return max(d for _h, d in russain_stacks)


def test():
    s = Solution()
    res = s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
    assert res == 3, res
    res = s.maxEnvelopes([[1, 1], [1, 1], [1, 1]])
    assert res == 1, res
    # fmt: off
    res = s.maxEnvelopes([[2,1],[4,1],[6,2],[8,3],[10,5],[12,8],[14,13],[16,21],[18,34],[20,55]])
    assert res == 9, res
    # fmt: on
    import random

    arr = [[random.randint(1, 1000), random.randint(1, 1000)] for _ in range(10000)]
    res = s.maxEnvelopes(arr)
