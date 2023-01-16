import bisect


class Solution:
    """
    You are given an array of non-overlapping intervals intervals where intervals[i] =
    [starti, endi] represent the start and the end of the ith interval and intervals is sorted
    in ascending order by starti. You are also given an interval newInterval = [start, end] that
    represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by
    starti and intervals still does not have any overlapping intervals (merge overlapping intervals
    if necessary).

    Return intervals after the insertion.

    Constraints:
        0 <= intervals.length <= 10^4
        intervals[i].length == 2
        0 <= starti <= endi <= 10^5
        intervals is sorted by start_i in ascending order.
        newInterval.length == 2
        0 <= start <= end <= 10^5
    """

    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        Unlisted constraint: intervals are non-overlapping
        O(n) / O(n)     time / space complexity
        """

        # find index where new interval would fit
        i = bisect.bisect(intervals, new_interval)
        # copy all intervals before interval into result list
        res = intervals[:i]

        if i > 0:
            if intervals[i-1][1] >= new_interval[0]:
                # if new interval intersects with an interval that comes before it,
                # extend the new interval if necessary
                prev_interval = res.pop()
                new_interval = [prev_interval[0], max(new_interval[1], prev_interval[1])]
        else:
            if len(intervals) > 0 and new_interval[1] >= intervals[0][0]:
                # if new interval is first interval, merge with first interval already
                # (not doing so causes failed edgecase, e.g. intervals=[[1,5]], new_interval=[0,3])
                new_interval[1] = max(new_interval[1], intervals[0][1])

        # find index of interval that new interval no longer overlaps
        while i < len(intervals) and new_interval[1] >= intervals[i][0]:
            i += 1

        # merge all overlapping intervals by updating the end coordinate of the new interval
        if i > 1:
            new_interval[1] = max(new_interval[1], intervals[i-1][1])

        # append the new interval to the result, and all larger remaining intervals
        res.append(new_interval)
        res.extend(intervals[i:])
        return res
