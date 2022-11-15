from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # attempt at union find with size turned into a mess, so this mess was created instead

        stones_tuple = [tuple(stone) for stone in stones]
        row_stones = defaultdict(set)
        col_stones = defaultdict(set)
        for stone in stones_tuple:
            row, col = stone
            row_stones[row].add(stone)
            col_stones[col].add(stone)

        visited = set()
        res = 0
        for stone in stones_tuple:
            row, col = stone
            if stone in row_stones[row]:
                tree_size = 0
                bfs_stack = [stone]
                while bfs_stack:
                    curr = bfs_stack.pop()
                    if curr in visited:
                        continue
                    visited.add(curr)
                    tree_size += 1
                    curr_row, curr_col = curr
                    bfs_stack.extend(row_stones[curr_row])
                    bfs_stack.extend(col_stones[curr_col])
                    row_stones[curr_row].clear()
                    col_stones[curr_col].clear()
                res += tree_size - 1

        return res