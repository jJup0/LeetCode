"""
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit].
Initially, all balls are uncolored. For every query in queries that is of the
form [x, y], you mark ball x with the color y. After each query, you need to
find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of
distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.

Constraints:
- 1 <= limit <= 10^9
- 1 <= n == queries.length <= 10^5
- queries[i].length == 2
- 0 <= queries[i][0] <= limit
- 1 <= queries[i][1] <= 10^9
"""

from collections import Counter


class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        """
        Complexity:
            Time: O(queries)
            Space: O(queries)
        """
        ball_to_color: dict[int, int] = {}
        color_counter: Counter[int] = Counter()
        res: list[int] = [0] * len(queries)
        unique_colors = 0
        for query_i, (ball, color) in enumerate(queries):
            prev_color = ball_to_color.get(ball, 0)
            if prev_color:
                # unpaint ball, update colors count
                color_counter[prev_color] -= 1
                if color_counter[prev_color] == 0:
                    unique_colors -= 1

            # paint ball with new color, update colors count
            ball_to_color[ball] = color
            if color_counter[color] == 0:
                unique_colors += 1
            color_counter[color] += 1

            res[query_i] = unique_colors
        return res
