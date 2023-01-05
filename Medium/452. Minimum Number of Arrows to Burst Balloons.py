class Solution:
    """
    There are some spherical balloons taped onto a flat wall that represents the XY-plane. The
    balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes
    a balloon whose horizontal diameter stretches between xstart and xend. You do not know the
    exact y-coordinates of the balloons.

    Arrows can be shot up directly vertically (in the positive y-direction) from different points
    along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if
    xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow
    keeps traveling up infinitely, bursting any balloons in its path.

    Given the array points, return the minimum number of arrows that must be shot to burst all
    balloons.

    Constraints:
        1 <= points.length <= 10^5
        points[i].length == 2
        -2^31 <= xstart < xend <= 2^31 - 1
    """

    def findMinArrowShots(self, points: list[list[int]]) -> int:
        """
        Sort balloons by end coordinate and shoot arrow at x_end coordinate. The "first ending"
        balloon needs to have an arrow shot through it, so shoot arrow at its ending coordinate,
        to maximize hits on other ballons. Find next "first ending" unshot balloon and repeat.

        O(n * log(n)) / O(1)    time / space complexity
        """

        # sort balloons by end coordinate
        points.sort(key=lambda x: x[1])

        # result variable
        res = 0

        # x coordinate of last arrow shot
        prev_arrow = float('-inf')

        for start, end in points:
            # if arrow not yet shot, shoot arrow at its ending coordinates
            if start > prev_arrow:
                res += 1
                prev_arrow = end

        return res
