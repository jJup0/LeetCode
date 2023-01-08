from collections import defaultdict
from fractions import Fraction


class Solution:
    """
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return
    the maximum number of points that lie on the same straight line.

    Constraints:
        1 <= points.length <= 300
        points[i].length == 2
        -10^4 <= xi, yi <= 10^4
        All the points are unique.
    """

    def maxPoints(self, points: list[list[int]]) -> int:
        """
        Draw lines from all possible pairs of points, and add points to dictionary where the key is
        the line's y-intercept and gradient, and the values are the points that lie on the line.
        O(n^2) / O(n^2)     time / space complexity
        """

        # dictionary for all lines that can be drawn from point segments
        lines = defaultdict(set)

        for i, p1 in enumerate(points):
            x1, y1 = p1
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                dx = x2 - x1
                if dx == 0:
                    # if two points have the same x coordinate, set gradient to infinity and
                    # yintercept to dummy value of the x coordinate
                    gradient = float('inf')
                    yintercept = x1
                else:
                    dy = y2 - y1

                    # Use fractions for gradient, floats can be messy! Built-in python fractions
                    # are automatically simplified. Floats are faster and accepted by leetcode
                    # tests but should not be used
                    gradient = Fraction(dy, dx)

                    # calculate yintercept for line, is of type Fraction
                    yintercept = -x1 * gradient + y1

                # add both points to the line
                line = (gradient, yintercept)
                lines[line].add((x1, y1))
                lines[line].add((x2, y2))

        # return amount of point on line with most points, default=1 if there is only 1 point
        return max((len(l) for l in lines.values()), default=1)
