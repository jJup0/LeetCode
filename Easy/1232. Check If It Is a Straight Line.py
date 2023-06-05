from fractions import Fraction


class Solution:
    """
    You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
    represents the coordinate of a point. Check if these points make a straight
    line in the XY plane.

        Constraints:
        2 <= coordinates.length <= 1000
        coordinates[i].length == 2
        -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
        coordinates contains no duplicate point.
    """

    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        different_xs = set(x for x, _ in coordinates)
        if len(different_xs) == 1:
            # all x values the same, all points on a vertical line (check needed for divide by 0)
            return True
        if len(different_xs) != len(coordinates):
            return False

        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        gradient = Fraction(y1 - y2, x1 - x2)
        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i]
            gradient2 = Fraction(y1 - y2, x1 - x2)
            if gradient != gradient2:
                return False
        return True
