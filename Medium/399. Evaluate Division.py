from collections import defaultdict, deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # define union-find data structure, with functions
        parent_of = {}

        def union(a, b):
            # O(1) amortized time
            parent_of[find(a)] = find(b)

        def find(x):
            curr_parent = parent_of[x]
            if curr_parent != x:
                parent_of[x] = find(curr_parent)
            return parent_of[x]
        # end of union find

        # dictionary of dictionaries to store divisions between variables
        divs = defaultdict(dict)
        # set divisions results for equations, and add pairs to union-find
        for value, (a, b) in zip(values, equations):
            divs[a][b] = value
            divs[b][a] = 1/value
            if a not in parent_of:
                parent_of[a] = a
            if b not in parent_of:
                parent_of[b] = b
            union(a, b)

        # function to connect variables and their quotients
        def bfs(start, goal):
            # track which variables have been added to avoid duplicates
            added_to_queue = set((start, ))
            # queue for bfs search, with variable and quotient of start/variable
            queue = deque(((start, 1), ))
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

        ret = []
        for a, b in queries:
            # if a or b never defined, or they have no connect, append default value -1
            if not (a in parent_of) or not (b in parent_of) or find(a) != find(b):
                ret.append(-1.0)
            else:
                ret.append(bfs(a, b))

        return ret
