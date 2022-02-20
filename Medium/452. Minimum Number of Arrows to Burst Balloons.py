class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        # ret = 0
        # i = 0
        # while i < len(points):
        #     _, x_end = points[i]
        #     i += 1
        #     while i < len(points) and points[i][0] <= x_end:
        #         i += 1
        #     ret += 1
        # return ret
        
        # same concept, but faster and cleaner
        res = 1
        tail = points[0][1]
        for i in points[1:]:
            if i[0] > tail:
                res += 1
                tail = i[1]
        return res