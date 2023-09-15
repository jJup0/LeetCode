import heapq


class Solution:
    """
    You are given an array points representing integer coordinates of some points
    on a 2D-plane, where points[i] = [xi, yi].

    The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
    between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

    Return the minimum cost to make all points connected. All points are connected
    if there is exactly one simple path between any two points.

    Constraints:
    - 1 <= points.length <= 1000
    - -10^6 <= xi, yi <= 10^6
    - All pairs (xi, yi) are distinct.
    """

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """
        Finds an MST using Prims algorithm.
        O(n^2) / O(n)   time / space complexity
        """
        max_int = 2 << 30
        # graph[i] = [shortest distance to exising MST, x, y]
        points_with_dist = [[max_int, x, y] for (x, y) in points]
        # start with "first" point, set its distance to 0 to use it as a starting node
        points_with_dist[0][0] = 0
        # result variable
        cost = 0
        # while points left to add to the graph
        while points_with_dist:
            # get vertex closest to existing MST and pop from heap
            dist, x, y = heapq.heappop(points_with_dist)
            # add its distance to the total cost
            cost += dist
            # update shortest distance to updated MST
            for neighbor in points_with_dist:
                old_dist, neighbor_x, neighbor_y = neighbor
                # calculate distance to current node
                dist_to_curr = abs(x - neighbor_x) + abs(y - neighbor_y)
                if dist_to_curr < old_dist:
                    # update shortest distance if smaller
                    neighbor[0] = dist_to_curr
            # heapify to make sure node with shortest distance is at the top of the heap
            heapq.heapify(points_with_dist)

        return cost
