"""
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest
vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the
y-axis (i.e., infinite height). The widest vertical area is the one with
the maximum width.

Note that points on the edge of a vertical area are not considered included
in the area.

Constraints:
- n == points.length
- 2 <= n <= 105
- points[i].length == 2
- 0 <= xi, yi <= 109
"""


class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        points.sort(key=lambda point: point[0])
        res = 0
        prev = points[0][0]
        for x, _y in points:
            width = x - prev
            if width > res:
                res = width
            prev = x
        return res
