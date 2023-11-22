from collections import deque
from dataclasses import dataclass
from typing import Iterator, cast


@dataclass
class LinkedListNode:
    nums_iter: Iterator[int]
    row_above: "LinkedListNode | None"
    row_below: "LinkedListNode | None"

    def delete(self):
        upper = self.row_above
        lower = self.row_below
        if upper:
            upper.row_below = lower
        if lower:
            lower.row_above = upper


class Solution:
    def findDiagonalOrder(self, numss: list[list[int]]) -> list[int]:
        """
        n := len(numss)
        m := sum(len(nums) for nums in numss)
        """
        return self.findDiagonalOrder_queue(numss)

    def findDiagonalOrder_queue(self, numss: list[list[int]]) -> list[int]:
        """
        O(m) / O(n)     time / space complexity
        """
        res: list[int] = []
        dq: deque[tuple[int, int]] = deque([(0, 0)])
        n = len(numss)
        while dq:
            # pop next position in grid from queue
            i, j = dq.popleft()
            res.append(numss[i][j])

            # every time first number of a list is reached, append first number of next row to queue
            next_row_idx = i + 1
            if j == 0 and next_row_idx < n:
                dq.append((next_row_idx, j))

            # if the numbers of the current row have not been exhausted yet append to queue
            next_col_idx = j + 1
            if next_col_idx < len(numss[i]):
                dq.append((i, next_col_idx))

        return res

    def findDiagonalOrder_linked_list(self, numss: list[list[int]]) -> list[int]:
        """
        O(m) / O(n)     time / space complexity
        """
        dummy_head = curr = LinkedListNode(iter([]), None, None)
        for nums in numss:
            list_node = LinkedListNode(iter(nums), curr, None)
            curr.row_below = list_node
            curr = list_node

        curr_starting_row: LinkedListNode = cast(LinkedListNode, dummy_head.row_below)

        res: list[int] = []
        while dummy_head.row_below is not None:
            curr_row: LinkedListNode = curr_starting_row
            while curr_row is not dummy_head:
                assert curr_row.row_above is not None
                next_num = next(curr_row.nums_iter, None)
                if next_num is None:
                    if curr_row.row_below is None:
                        curr_starting_row = curr_row.row_above
                    curr_row.delete()
                else:
                    res.append(next_num)
                curr_row = curr_row.row_above
            curr_starting_row = curr_starting_row.row_below or curr_starting_row
        return res
