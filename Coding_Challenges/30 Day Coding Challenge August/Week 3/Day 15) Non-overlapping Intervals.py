class Solution:
    def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        lastIntervalEnd = intervals[0][0] - 1
        maxNonoverlapIntervals = 0
        for interval in intervals:
            if lastIntervalEnd > interval[0]:
                lastIntervalEnd = min(lastIntervalEnd, interval[1])
            else:
                maxNonoverlapIntervals += 1
                lastIntervalEnd = interval[1]
        return len(intervals) - maxNonoverlapIntervals
