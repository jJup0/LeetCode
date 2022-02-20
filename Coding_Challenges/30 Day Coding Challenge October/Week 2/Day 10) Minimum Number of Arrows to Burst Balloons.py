# import bisect
# class Solution:
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         points.sort(key = lambda x: x[1])
#         n = len(points)
#         i = 0
#         res = 0
#         while i < n:
#             end = points[i][1]
#             while i < n and end >= points[i][0]:
#                 i += 1
#             res += 1
#         return res
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        next_end = float("-inf")
        res = 0
        for cur_start, cur_end in points:
            if cur_start > next_end:
                next_end = cur_end
                res += 1
        return res
