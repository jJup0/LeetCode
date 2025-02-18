"""
You have n tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using
the letters printed on those tiles.

Constraints:
- 1 <= tiles.length <= 7
- tiles consists of uppercase English letters.
"""

import functools
import itertools
import operator
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Should be possible in O(n) I think, but I'm too lazy to figure it out right now.
        Complexity:
            Time: O(n!)
            Space: O(n!)
        """
        # self.checked contains all the substrings for which
        # _numTilePossibilities() has already been calculated
        self.checked: set[str] = set()
        possibilities = self._numTilePossibilities("".join(sorted(tiles)))
        return len(possibilities)

    def _numTilePossibilities(self, tiles: str) -> set[str]:
        if tiles in self.checked:
            # no need to add to result again
            return set()
        if len(tiles) == 1:
            return {tiles}

        combos = set(
            "".join(perm) for perm in itertools.permutations(tiles, len(tiles))
        )
        tiles_list = list(tiles)
        for i in range(len(tiles_list)):
            char = tiles_list[i]
            tiles_list[i] = ""
            combos.update(self._numTilePossibilities("".join(tiles_list)))
            tiles_list[i] = char

        self.checked.add(tiles)
        return combos


class SolutionMath:
    """
    More mathematical approach using multiset calculations.
    """

    def numTilePossibilities(self, tiles: str) -> int:
        factorial_lookup = [1]
        for i in range(1, len(tiles) + 1):
            factorial_lookup.append(factorial_lookup[-1] * i)

        freq_values = list(Counter(tiles).values())
        return sum(
            factorial_lookup[k]
            // functools.reduce(operator.mul, (factorial_lookup[f] for f in subset))
            for k in range(1, len(tiles) + 1)
            for subset in self.generate_subsets(freq_values, k)
        )

    def generate_subsets(self, freq_values: list[int], k: int) -> list[list[int]]:
        """Generate all subsets of counts summing to k"""
        if k == 0:
            return [[]]
        if not freq_values:
            return []
        last = freq_values.pop()
        subsets: list[list[int]] = []
        for i in range(min(k, last) + 1):
            for subset in self.generate_subsets(freq_values, k - i):
                subsets.append([i] + subset)
        freq_values.append(last)
        return subsets


def test():
    import random
    import time

    sol1 = Solution()
    sol2 = SolutionMath()

    alphabet = [chr(ord_nr) for ord_nr in range(ord("a"), ord("z") + 1)]
    for i in range(1, 11):
        string = "".join(random.choice(alphabet) for _ in range(i))
        t1 = time.perf_counter_ns()

        res1 = sol1.numTilePossibilities(string)
        t2 = time.perf_counter_ns()
        print(f"Alg 1, size={i}, result={res1}, time={(t2 - t1) / 1_000_000}ms")

        res2 = sol2.numTilePossibilities(string)
        t3 = time.perf_counter_ns()
        print(f"Alg 2, size={i}, result={res2}, time={(t3 - t2) / 1_000_000}ms")

        assert res1 == res2
        print("-" * 20)


if __name__ == "__main__":
    test()
