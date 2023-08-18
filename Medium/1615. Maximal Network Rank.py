class Solution:
    """
    There is an infrastructure of n cities with some number of roads connecting
    these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional
    road between cities ai and bi.

    The network rank of two different cities is defined as the total number of
    directly connected roads to either city. If a road is directly connected to both
    cities, it is only counted once.

    The maximal network rank of the infrastructure is the maximum network rank of
    all pairs of different cities.

    Given the integer n and the array roads, return the maximal network rank of
    the entire infrastructure.

    Constraints:
    - 2 <= n <= 100
    - 0 <= roads.length <= n * (n - 1) / 2
    - roads[i].length == 2
    - 0 <= ai, bi <= n-1
    - a_i != b_i
    - Each pair of cities has at most one road connecting them.
    """

    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        # create adjacency lists
        neighbors: list[set[int]] = [set() for _ in range(n)]
        for a, b in roads:
            neighbors[a].add(b)
            neighbors[b].add(a)

        # sort cities by neighbor count descending
        neighbors_sorted = sorted(enumerate(neighbors), key=lambda x: -len(x[1]))

        result = 0
        # iterate through pairs of neighbors
        for j, (a, a_neighbors) in enumerate(neighbors_sorted):
            for i in range(j):
                b, b_neighbors = neighbors_sorted[i]

                score = len(a_neighbors) + len(b_neighbors)
                if score <= result:
                    # can break early if score will never beat current result
                    break

                # cities share an edge if they are neighbors, in that case decrement the score
                score -= b in a_neighbors

                # update result if score is best so far
                if score > result:
                    result = score

        return result
