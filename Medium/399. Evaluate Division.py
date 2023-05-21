from collections import defaultdict, deque


class UnionFind:
    def __init__(self) -> None:
        self.parent_of: dict[str, str] = {}

    def union(self, a: str, b: str):
        # O(1) amortized time
        self.parent_of[self.find(a)] = self.find(b)

    def find(self, x: str) -> str:
        curr_parent = self.parent_of[x]
        if curr_parent != x:
            self.parent_of[x] = self.find(curr_parent)
        return self.parent_of[x]


class Solution:
    """
    You are given an array of variable pairs equations and an array of real numbers
    values, where equations[i] = [Ai, Bi] and values[i] represent the equation
    Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

    You are also given some queries, where queries[j] = [Cj, Dj] represents the jth
    query where you must find the answer for Cj / Dj = ?.

    Return the answers to all queries. If a single answer cannot be determined, return -1.0.

    Note: The input is always valid. You may assume that evaluating the queries
    will not result in division by zero and that there is no contradiction.

    Constraints:
        1 <= equations.length <= 20
        equations[i].length == 2
        1 <= Ai.length, Bi.length <= 5
        values.length == equations.length
        0.0 < values[i] <= 20.0
        1 <= queries.length <= 20
        queries[i].length == 2
        1 <= Cj.length, Dj.length <= 5
        Ai, Bi, Cj, Dj consist of lower case English letters and digits.
    """

    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        # function to connect variables and their quotients
        def bfs(start: str, goal: str) -> float:
            nonlocal divs
            # track which variables have been added to avoid duplicates
            added_to_queue = set((start,))
            # queue for bfs search, with variable and quotient of start/variable
            queue: deque[tuple[str, float]] = deque(((start, 1),))
            while queue:
                # get variable from queue
                x, div = queue.popleft()

                # if variable is goal, return quotient
                if x == goal:
                    return div

                # go through neighbors of variable to find goal variable and define quotients along the way
                for neighbor, new_div in divs[x].items():
                    if not neighbor in added_to_queue:
                        # start/neighbor is euqal to old quotient times quotient from variable to neighbor
                        queue.append((neighbor, div * new_div))
                        divs[start][neighbor] = div * new_div
                        added_to_queue.add(neighbor)

            assert False

        UF = UnionFind()

        # dictionary of dictionaries to store divisions between variables
        divs: dict[str, dict[str, float]] = defaultdict(dict)
        # set divisions results for equations, and add pairs to union-find
        for value, (a, b) in zip(values, equations):
            divs[a][b] = value
            divs[b][a] = 1 / value
            if a not in UF.parent_of:
                UF.parent_of[a] = a
            if b not in UF.parent_of:
                UF.parent_of[b] = b
            UF.union(a, b)

        ret: list[float] = []
        for a, b in queries:
            # if a or b never defined, or they have no connect, append default value -1
            if (
                a not in UF.parent_of
                or b not in UF.parent_of
                or UF.find(a) != UF.find(b)
            ):
                ret.append(-1.0)
            else:
                ret.append(bfs(a, b))

        return ret
