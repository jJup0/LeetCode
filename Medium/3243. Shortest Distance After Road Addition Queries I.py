"""
You are given an integer n and a 2D integer array queries.

There are n cities numbered from 0 to n - 1. Initially, there is a
unidirectional road from city i to city i + 1 for all 0 <= i < n - 1.

 queries[i] = [u_i, v_i] represents the addition of a new unidirectional road
from city u_i to city v_i. After each query, you need to find the length of the
shortest path from city 0 to city n - 1.

Return an array answer where for each i in the range [0, queries.length - 1],
answer[i] is the length of the shortest path from city 0 to city n - 1 after
processing the first i + 1 queries.

Constraints:
- 3 <= n <= 500
- 1 <= queries.length <= 500
- queries[i].length == 2
- 0 <= queries[i][0] < queries[i][1] < n
- 1 < queries[i][1] - queries[i][0]
- There are no repeated roads among the queries.
"""


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        """
        Naive BFS after each query
        Complexity:
            Time: O(m * (n + m))
            Space: O(n + m)
        """
        jumps = [[i] for i in range(1, n + 1)]
        res: list[int] = []
        for a, b in queries:
            jumps[a].append(b)
            res.append(self._get_min_jumps(jumps))
        return res

    def _get_min_jumps(self, jumps: list[list[int]]) -> int:
        """
        Simple BFS to get from city 0 to n-1.
        Complexity:
            Time: O(n + m)
            Space: O(n + m)
        """
        last_city = len(jumps) - 1
        steps = 0
        visited = [False] * len(jumps)
        current_cities = [0]
        while True:
            next_cities: list[int] = []
            for pos in current_cities:
                if pos == last_city:
                    return steps
                if visited[pos]:
                    continue
                visited[pos] = True
                next_cities.extend(jumps[pos])
            current_cities = next_cities
            steps += 1
