"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string
colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons
to be of the same color, so she asks Bob for help. Bob can remove some balloons
from the rope to make it colorful. You are given a 0-indexed integer array
neededTime where neededTime[i] is the time (in seconds) that Bob needs to
remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

Constraints:
- n == colors.length == neededTime.length
- 1 <= n <= 10^5
- 1 <= neededTime[i] <= 10^4
- colors contains only lowercase English letters.
"""


class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """

        # previous character during iteration
        prev_color = colors[0]
        res = sum(neededTime)
        # running and lowest cost of consecutive balloons
        highest_cost = 0

        for color, cost in zip(colors, neededTime):
            if color == prev_color:
                if cost > highest_cost:
                    highest_cost = cost
            else:
                res -= highest_cost
                highest_cost = cost
                prev_color = color

        return res - highest_cost


s = Solution()
print(s.minCost("abaac", [1, 2, 3, 4, 5]))
