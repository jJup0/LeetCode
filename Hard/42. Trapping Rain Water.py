"""
Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it can trap after raining.

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""


class Solution:
    def trap(self, heights: list[int]) -> int:
        """
        when the term "lowest height of untrapped water" is used, this is what is meant:
        4 █ - - -
        3 █ - - -
        2 █ w █ ~
        1 █ w █ ~
          0 1 2 3 ...

        'w' marks water trapped, '~' untrapped water that will be trapped with wall at index 2,
        '-' untrapped water that will be trapped with wall at index 0
        at index three the lowest untrapped height for wall_0 is 2, and for wall_2 it is 0

        O(n) / O(n)     time / space complexity
        """

        # result variable
        water = 0

        # stack to track previous walls, always in decreasing order of height
        # stack[i] = [idx, starting_height, actual_height]
        stack: list[list[int]] = []

        for i, h in enumerate(heights):
            # while this wall is taller/equal the previous wall (on stack), pop it from the stack
            # and fill water between that wall and the current wall
            while stack and stack[-1][2] <= h:
                j, h1, h2 = stack.pop()
                water += (i - j - 1) * (h2 - h1)

            # if this wall is high enough to create a barrier with the the previous wall, to trap
            # water, add this water to the total, and update the lowest height of untrapped water
            # for the wall on the stack
            if stack and stack[-1][1] < h:
                j, h1, _ = stack[-1]
                water += (i - j - 1) * (h - h1)
                stack[-1][1] = h

            # add this wall to the stack, with lowest point unfilled at
            stack.append([i, 0, h])

        return water

    def trap_stolen(self, heights: list[int]) -> int:
        """
        stolen, but commented and minimally adapted O(1)-space solution, trap water from both sides,
        fill each index one by one.
        O(n) / O(1)     time / space complexity
        """
        if not heights:
            return 0

        # left and right index for sliding window
        l, r = 0, len(heights) - 1

        # invariant: left_max = max(heights[:l+1], right_max = max(heights[r:])
        left_max, right_max = heights[l], heights[r]

        # result variable
        res = 0

        while l < r:
            if left_max < right_max:
                # if the left wall is lower, move left border of sliding window one step to the right
                l += 1
                h_l = heights[l]
                if h_l > left_max:
                    # if new left wall is higher, update max height
                    left_max = h_l
                else:
                    # otherwise fill current index with water (left_max is still less than right_max)
                    res += left_max - h_l
            else:
                # analog if right wall is lower
                r -= 1
                h_r = heights[r]
                if h_r > right_max:
                    right_max = h_r
                else:
                    res += right_max - h_r

        return res
