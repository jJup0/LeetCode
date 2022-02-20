class Solution:
    def checkStraightLine(self, coordinates: [[int]]) -> bool:
        m = (coordinates[1][0] - coordinates[0][0])/(coordinates[1][1] - coordinates[1][0])
        i = 2
        while i < len(coordinates):
            if (coordinates[i][0] - coordinates[i-1][0])/(coordinates[i][1] - coordinates[i-1][0]) != m:
                return False
            i += 1
        return True
