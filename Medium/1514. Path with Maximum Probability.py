import heapq


class Solution:
    """
    You are given an undirected weighted graph of n nodes (0-indexed), represented
    by an edge list where edges[i] = [a, b] is an undirected edge connecting the
    nodes a and b with a probability of success of traversing that edge succProb[i].

    Given two nodes start and end, find the path with the maximum probability of
    success to go from start to end and return its success probability.

    If there is no path from start to end, return 0. Your answer will be accepted
    if it differs from the correct answer by at most 1e-5.

    Constraints:
    - 2 <= n <= 10^4
    - 0 <= start, end < n
    - start != end
    - 0 <= a, b < n
    - a != b
    - 0 <= succProb.length == edges.length <= 2*10^4
    - 0 <= succProb[i] <= 1
    - There is at most one edge between every two nodes.
    """

    def maxProbability(
        self,
        n: int,
        edges: list[list[int]],
        succProb: list[float],
        start: int,
        end: int,
    ) -> float:
        """Dijkstra search.
        O((n + m) * log(n)) / O(m)  time / space complexity
        """
        # build adjacency lists
        adj: dict[int, dict[int, float]] = {i: {} for i in range(n)}
        for (a, b), prob in zip(edges, succProb):
            adj[a][b] = prob
            adj[b][a] = prob

        # initially, the highest probability of reaching any node is 0
        best_prob = [0.0] * n
        # reaching start has probability 1.
        # priority queue as a max-heap, by negating the actual probability
        prio_queue = [(-1.0, start)]
        while prio_queue:
            negtive_prob, pos = heapq.heappop(prio_queue)
            # get actual probability by negating
            prob = -negtive_prob
            # if end node reached, the highest probability has been found,
            # due to using a priority queue
            if pos == end:
                return prob

            # traverse to neighbors
            for neighbor, edge_prob in adj[pos].items():
                prob_for_neighbor = prob * edge_prob
                # only add to queue if the probability is lower than the current best
                if prob_for_neighbor > best_prob[neighbor]:
                    best_prob[neighbor] = prob_for_neighbor
                    heapq.heappush(prio_queue, (-prob_for_neighbor, neighbor))

        # if end is unreachable, return 0
        return 0.0
