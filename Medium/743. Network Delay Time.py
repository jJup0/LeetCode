import heapq
from collections import defaultdict
from typing import List


class Solution:
    """
    You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel
    times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
    and wi is the time it takes for a signal to travel from source to target.
    We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the
    signal. If it is impossible for all the n nodes to receive the signal, return -1.
    Constraints:
        1 <= k <= n <= 100
        1 <= times.length <= 6000
        times[i].length == 3
        1 <= ui, vi <= n
        ui != vi
        0 <= wi <= 100
        All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dictionary to track connections and their weights
        times_dict = defaultdict(list)
        for u, v, w in times:
            # constraint: no duplicates in times
            times_dict[u].append((v, w))

        # dist[i] has distance from node k to i
        dist = [float("inf")] * (n + 1)

        # nodes are 1 indexed, so set dist[0] to 0, dist[k] trivially 0
        dist[0] = dist[k] = 0

        # queue for "uniform cost search", fibonnaci queue would be better, but no native implementation
        bfs_front = [(w, v) for v, w in times_dict[k]]
        heapq.heapify(bfs_front)

        # go through all nodes in O(times)
        while bfs_front:
            # pop node and distance to get there from queue
            dist_so_far, u = heapq.heappop(bfs_front)

            # if the distance is lower than the lowest distance (u has never been visited)
            if dist_so_far < dist[u]:
                # update it lowest distance to node
                dist[u] = dist_so_far
                # go through neighbors and add them to the priority queue if distance to get there is lower than
                # distance stored there so far
                for v, w in times_dict[u]:
                    new_weight = dist_so_far + w
                    if new_weight < dist[v]:
                        heapq.heappush(bfs_front, (new_weight, v))

        return (-1) if (float("inf") in dist) else max(dist)    # type: ignore , can only be float if 'inf' in dist
