"""
You are given an integer n denoting the number of cities in a country. The
cities are numbered from 0 to n - 1.

You are also given a 2D integer array roads where roads[i] = [a_i, b_i] denotes
that there exists a bidirectional road connecting cities a_i and b_i.

You need to assign each city with an integer value from 1 to n, where each
value can only be used once. The importance of a road is then defined as the
sum of the values of the two cities it connects.

Return the maximum total importance of all roads possible after assigning the
values optimally.

Constraints:
- 2 <= n <= 5 * 10^4
- 1 <= roads.length <= 5 * 10^4
- roads[i].length == 2
- 0 <= a_i, b_i <= n - 1
- a_i!= b_i
- There are no duplicate roads.
"""


class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        """
        O(n * log(n)) / O(n)    time space complexity
        """
        # get degree (number of connections) of each city in the graph
        city_to_degree = [0] * n
        for a, b in roads:
            city_to_degree[a] += 1
            city_to_degree[b] += 1

        # sort by degree and greedily assign highest importance to city with highest degree
        city_to_degree.sort()
        return sum(
            importance * degree
            for importance, degree in enumerate(city_to_degree, start=1)
        )
