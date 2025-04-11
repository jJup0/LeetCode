"""
Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1, return the area of the largest rectangle in
the histogram.

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""

import itertools
from dataclasses import dataclass


class Solution4:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Proper implementation of Solution1 where monotone stack is used efficiently.
        Stolen and refactored from someone else's submission.

        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def form_rectangle_with_top_of_stack(bar_position: int):
            nonlocal heights, ans, stack
            height = heights[stack.pop()]
            if stack:
                width = bar_position - stack[-1] - 1
            else:
                width = bar_position
            ans = max(ans, height * width)
            return ans

        n = len(heights)
        ans = 0
        # list of indexes in heights, monotone increasing in terms of height,
        # for equal heights store last index
        stack: list[int] = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                form_rectangle_with_top_of_stack(i)
            stack.append(i)

        while stack:
            form_rectangle_with_top_of_stack(n)
        return ans


@dataclass(slots=True)
class BarNode:
    left: "BarNode | None"
    right: "BarNode | None"
    height: int
    width: int = 1

    def merge_into_taller_neighbor(self) -> None:
        if self.left is None and self.right is None:
            # last bar
            return

        # merge node into taller of the two neighbor nodes
        if self.left and (not self.right or (self.left.height > self.right.height)):
            self.left.width += self.width
        else:
            assert self.right is not None
            self.right.width += self.width

        # delete node by making neighbors point at each other
        if self.left:
            self.left.right = self.right
        if self.right:
            self.right.left = self.left


class Solution3:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Create a linked list structure for all bars.
        Rectangles are created by merging bars into single wider bars.
        Iterate through bars in height order descending. After each step
        merge the bar into the taller of its neighbors, increasing the
        width of its neighbor by its current width.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        bars = [BarNode(None, None, h, 1) for h in heights]
        for bar_left, bar_right in itertools.pairwise(bars):
            bar_left.right = bar_right
            bar_right.left = bar_left

        bars.sort(key=lambda bar: bar.height, reverse=True)
        res = 0
        for bar in bars:
            res = max(res, bar.height * bar.width)
            # note this method causes side effects for its neighbors
            bar.merge_into_taller_neighbor()
        return res


class Solution2:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Original implementation that used linked list, but storing
        everything in arrays, made it very error prone and hard to
        debug. Faster in practicethan Solution3 but less explicit.
        """
        # pseudo doubly-linked-list structure, -1 means no neighbor
        neighbor_left = list(range(-1, len(heights) - 1))
        neighbor_right = list(range(1, len(heights) + 1))
        neighbor_right[-1] = -1
        # multiplier[i] = amount of bars that have merged into bar i
        bar_width = [1] * len(heights)

        res = 0
        heights_sorted = sorted(((h, i) for i, h in enumerate(heights)), reverse=True)
        for h, i in heights_sorted:
            res = max(res, h * bar_width[i])

            # update linked list structure
            l = neighbor_left[i]
            r = neighbor_right[i]
            height_l = height_r = -1
            if l != -1:
                height_l = heights[l]
            if r != -1:
                height_r = heights[r]

            # could check here if `height_l == height_r == -1` and skip
            # merging for the last bar standing, but no need

            # merge node into
            if height_l < height_r:
                bar_width[r] += bar_width[i]
            else:
                bar_width[l] += bar_width[i]
            # delete node by making neighbors point at each other
            if l != -1:
                neighbor_right[l] = r
            if r != -1:
                neighbor_left[r] = l

            # for debugging, can update current node, but not needed
            # neighbor_left[i] = neighbor_right[i] = heights[i] = -1
            # multiplier[i] = 0

            # self._linked_list_sanity_check(neighbor_left, neighbor_right, multiplier)

        return res

    def _linked_list_sanity_check(
        self, neighbor_left: list[int], neighbor_right: list[int], multiplier: list[int]
    ):
        """Checks if pseudo linked list structure is intact."""
        assert neighbor_right[-1] == -1, neighbor_right
        assert neighbor_left[0] == -1, neighbor_left
        assert sum(multiplier) == len(multiplier), multiplier

        for node, r in enumerate(neighbor_right):
            if r != -1:
                assert neighbor_left[r] == node

        first_node = 0
        for first_node, r in enumerate(neighbor_right):
            if r != -1:
                break
        steps = 0
        while first_node != -1 and steps < len(neighbor_right):
            first_node = neighbor_right[first_node]
            steps += 1
        assert first_node == -1, neighbor_right


class Solution1:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        Keep a monotone increasing stack of heights and at
        each bar build rectangles with each bar in the stack.

        Complexity:
            Time: O(n^2)
            Space: O(n)
        """
        monotone_inc_stack = [(0, 0)]
        res = 0
        for i, h in enumerate(heights):
            last_i = i
            while monotone_inc_stack[-1][0] > h:
                last_i = monotone_inc_stack.pop()[1]
                res = max(res, h * (i - last_i + 1))

            res = max(
                res,
                h,
                max(
                    prev_height * (i - idx + 1)
                    for prev_height, idx in monotone_inc_stack
                ),
            )

            if h > monotone_inc_stack[-1][0]:
                monotone_inc_stack.append((h, last_i))
        return res


class Solution(Solution4):
    pass


def test():
    import time

    s = Solution4()
    res = s.largestRectangleArea([2, 3, 3, 2])
    assert res == 8, res
    res = s.largestRectangleArea([5, 4])
    assert res == 8, res
    res = s.largestRectangleArea([2, 1, 5, 6, 2, 2, 2, 2])
    assert res == 12, res
    res = s.largestRectangleArea([5, 4, 4, 6, 3, 2, 9, 5, 4, 8, 1, 0, 0, 4, 7, 2])
    assert res == 20, res

    arr = list(range(100000)) * 10
    s1 = time.perf_counter_ns()
    res = s.largestRectangleArea(arr)
    s2 = time.perf_counter_ns()
    print(res, (s2 - s1) / 1_000_000_000)
