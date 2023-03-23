class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]

    def find(self, city) -> int:
        if self.parents[city] != city:
            self.parents[city] = self.find(self.parents[city])
        return self.parents[city]

    def union(self, a, b) -> None:
        a_parent = self.find(a)
        b_parent = self.find(b)
        self.parents[a_parent] = b_parent


class Solution:
    """
    There are n computers numbered from 0 to n - 1 connected by ethernet cables
    connections forming a network where connections[i] = [ai, bi] represents a
    connection between computers ai and bi. Any computer can reach any other computer
    directly or indirectly through the network.

    You are given an initial computer network connections. You can extract certain cables
    between two directly connected computers, and place them between any pair of
    disconnected computers to make them directly connected.

    Return the minimum number of times you need to do this in order to make all the computers
    connected. If it is not possible, return -1.

    Constraints:
        1 <= n <= 10^5
        1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
        connections[i].length == 2
        0 <= a_i, b_i < n
        a_i != b_i
        There are no repeated connections.
        No two computers are connected by more than one cable.
    """

    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        """
        Uses union find to determine the amount of disjoint sets. Every disjoint
        set needs a single connection to join the "main"/"base" network.
        O(m * log(n)) / O(n)     time / space complexity
        """

        # need at least n-1 connections to connect all pcs
        if len(connections) < n - 1:
            return -1

        # form union between all pcs that share a connection
        union_find = UnionFind(n)
        for pc1, pc2 in connections:
            union_find.union(pc1, pc2)

        # find how many disjoint sets there are, by checking
        # how many different parents there are
        different_parents = set(union_find.find(i) for i in range(n))

        # every extra disjoint set needs exactly one
        # cable to join the whole network
        return len(different_parents) - 1
