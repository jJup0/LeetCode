from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0], -x[1]))
        # sort intervals such that for indexes i < j, a[i] can not be overlapped by a[j], and a[j] will 
        # be overlapped if the is a k such that k < j and a[k][1] >= a[j][1]
        res = len(intervals)
        prev_end = intervals[0][1]

        for _, end in intervals[1:]:
            if end <= prev_end:
                res -= 1
            else:
                prev_end = end

        return res
