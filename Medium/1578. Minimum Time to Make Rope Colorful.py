from typing import List


class Solution:
    """
    Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where
    colors[i] is the color of the ith balloon.
    Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the
    same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it
    colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time
    (in seconds) that Bob needs to remove the ith balloon from the rope.
    Return the minimum time Bob needs to make the rope colorful.

    Constraints:
        n == colors.length == neededTime.length
        1 <= n <= 10^5
        1 <= neededTime[i] <= 10^4
        colors contains only lowercase English letters.
    """

    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        # returns an iterator object over neededTime[l:r] without slicing to avoid O(n) extra space
        def neededTime_iter(l, r):
            return (neededTime[i] for i in range(l, r))

        # previous character during iteration
        prev_c = colors[0]

        # result variable
        res = 0

        # left index of current same color balloon series
        l = 0

        for r, c in enumerate(colors):
            # if current color is different to previous
            if c != prev_c:
                # remove all but one balloon in the current series, do not remove the most
                # expensive balloon
                res += sum(neededTime_iter(l, r)) - max(neededTime_iter(l, r))

                # update "previous" color
                prev_c = c

                # update left index of current color
                l = r

        # remove last series of balloons
        res += sum(neededTime_iter(l, len(neededTime) - 1)) - max(neededTime_iter(l, len(neededTime) - 1))

        return res
