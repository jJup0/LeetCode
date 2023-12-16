"""
You are given the array paths, where paths[i] = [cityA_i, cityB_i] means
there exists a direct path going from cityA_i to cityB_i. Return the
destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop,
therefore, there will be exactly one destination city.

Constraints:
- 1 <= paths.length <= 100
- paths[i].length == 2
- 1 <= cityA_i.length, cityB_i.length <= 10
- cityA_i != cityB_i
- All strings consist of lowercase and uppercase English letters and the space character.
"""


class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        """
        O(total_chars) / O(total_chars)     time / space complexity
        """
        leave: set[str] = set()
        arrived: set[str] = set()
        for a, b in paths:
            leave.add(a)
            arrived.add(b)
        return arrived.difference(leave).pop()
