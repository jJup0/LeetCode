"""
You are given two integers m and n. Consider an m x n grid where each cell is
initially white. You can paint each cell red, green, or blue. All cells must be
painted.

Return the number of ways to color the grid with no two adjacent cells having
the same color. Since the answer can be very large, return it modulo 10^9 + 7.

Constraints:
- 1 <= m <= 5
- 1 <= n <= 1000
"""


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        """
        Precompute all valid columns and their compatibility with one another.

        Complexity:
            Time: O(2**m * n)
            Space: O(2**m)
        """
        MOD = 10**9 + 7
        compatibles = self.get_compatible_columns(m)
        curr_count = {coloring: 1 for coloring in compatibles}
        for _ in range(n - 1):
            new_count = {coloring: 0 for coloring in compatibles}
            for coloring, count in curr_count.items():
                for compatible in compatibles[coloring]:
                    new_count[compatible] += count
                    new_count[compatible] %= MOD
            curr_count = new_count
        return sum(curr_count.values()) % MOD

    def get_column_colorings(self, m: int):
        colorings = ["a", "b", "c"]
        for _ in range(m - 1):
            new_colorings: list[str] = []
            for color in colorings:
                for new_c in "abc":
                    if new_c != color[-1]:
                        new_colorings.append(color + new_c)
            colorings = new_colorings
        return colorings

    def get_compatible_columns(self, m: int):
        colorings = self.get_column_colorings(m)
        mapping: dict[str, list[str]] = {}
        for coloring in colorings:
            compatible: list[str] = []
            for second_coloring in colorings:
                if all(c1 != c2 for c1, c2 in zip(coloring, second_coloring)):
                    compatible.append(second_coloring)
            mapping[coloring] = compatible
        return mapping


def test():
    sol = Solution()
    res = sol.colorTheGrid(2, 1)
    print(res)
    res = sol.colorTheGrid(5, 5)
    print(res)
