"""
You are given a 2D array coords of size n x 2, representing the coordinates of
n points in an infinite Cartesian plane.

Find twice the maximum area of a triangle with its corners at any three
elements from coords, such that at least one side of this triangle is parallel
to the x-axis or y-axis. Formally, if the maximum area of such a triangle is A,
return 2 * A.

If no such triangle exists, return -1.

Note that a triangle cannot have zero area.

Constraints:
- 1 <= n == coords.length <= 10^5
- 1 <= coords[i][0], coords[i][1] <= 10^6
- All coords[i] are unique.
"""


class Solution:
    def maxArea(self, coords: list[list[int]]) -> int:
        """
        Complexity:
            Time: O(n * log(n))
            Space: O(sort)
        """
        # Sort coords so coordinates with same x-value (a pair of these form the
        # vertical edge) are next to each other and the leftmost and right most
        # point (forming the largest triangle possible for each vertical line)
        # are the first and last coordinates.
        coords.sort()
        max_vertical = self._find_biggest_triangle(coords)

        # Switch around x and y coordinates and go again
        for coord in coords:
            coord.reverse()
        coords.sort()
        max_horizontal = self._find_biggest_triangle(coords)

        # Return maximum of the two or -1 if triangle of area 0 is found
        res = max(max_vertical, max_horizontal)
        if res == 0:
            return -1
        return res

    def _find_biggest_triangle(self, coords: list[list[int]]):
        prev_x = prev_y = -1
        res = -1
        for x, y in coords:
            if x != prev_x:
                # Cannot form triangle with previous coordinate
                prev_x = x
                prev_y = y
                continue
            # Make vertical edges with coordinate with same x-value and smallest
            # y-value (guaranteed due to sorting and setting y value once).
            # Then connect to leftmost and rightmost point to get largest triangle
            res = max(res, (y - prev_y) * (coords[-1][0] - x))
            res = max(res, (y - prev_y) * (x - coords[0][0]))
        return res


def test():
    s = Solution()
    res = s.maxArea([[5, 3], [7, 4], [8, 4]])
    real = 1
    assert res == real, res


test()
