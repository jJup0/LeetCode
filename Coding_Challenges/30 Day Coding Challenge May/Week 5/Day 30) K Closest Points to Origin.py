class mySolution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:
        i = 0
        ordered = set()
        for x, y in points:
            ordered.add((i, x**2 + y**2))
            i += 1
        ordered = sorted(ordered, key=lambda l: l[1])
        retVal = []
        for i in range(K):
            retVal.append(points[ordered[i][0]])
        return retVal


class Solution:
    def kClosest(self, points: [[int]], K: int) -> [[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]
