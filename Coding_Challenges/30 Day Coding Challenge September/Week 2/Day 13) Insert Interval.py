import bisect


class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        i = bisect.bisect(intervals, newInterval)
        if i > 0 and intervals[i-1][1] >= newInterval[0]:
            intervals[i-1][1] = max(newInterval[1], intervals[i-1][1])
        else:
            intervals.insert(i, newInterval)
            i += 1
        hi_at_prev = intervals[i-1][1]
        while i < len(intervals) and hi_at_prev >= intervals[i][0]:
            hi_at_prev = max(hi_at_prev, intervals[i][1])
            del intervals[i]
        intervals[i-1][1] = hi_at_prev
        return intervals
