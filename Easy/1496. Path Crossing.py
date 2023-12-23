"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing
moving one unit north, south, east, or west, respectively. You start at the
origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you
are on a location you have previously visited. Return false otherwise.

Constraints:
- 1 <= path.length <= 10^4
- path[i] is either 'N', 'S', 'E', or 'W'.
"""


class Solution:
    def isPathCrossing(self, path: str) -> bool:
        """
        O(n) / O(n)     time / space complexity
        """
        visited: set[tuple[int, int]] = set([(0, 0)])
        x = y = 0
        for direction in path:
            match direction:
                case "N":
                    y += 1
                case "E":
                    x += 1
                case "S":
                    y -= 1
                case "W":
                    x -= 1
                case _:
                    raise ValueError()
            point = (x, y)
            if point in visited:
                return True
            visited.add(point)
        return False


s = Solution()

print(s.isPathCrossing("NESWW"))
