"""
You are given an array of non-overlapping intervals intervals where
intervals[i] = [start_i, end_i] represent the start and the end of the ith
interval and intervals is sorted in ascending order by start_i. You are also
given an interval newInterval = [start, end] that represents the start and end
of another interval.

Insert newInterval into intervals such that intervals is still sorted in
ascending order by start_i and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array
and return it.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^5
- intervals is sorted by start_i in ascending order.
- newInterval.length == 2
- 0 <= start <= end <= 10^5
"""


class Solution:
    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        """
        O(n) / O(n)     time / space complexity
        """
        if not intervals:
            return [new_interval]

        res: list[list[int]] = []

        new_start, new_stop = new_interval
        i = 0
        # append all strictly smaller intervals to result
        for i, interval in enumerate(intervals):
            if interval[1] >= new_start:
                # if an interval's end is larger than the start, then this interval
                # could be merged into the new interval, do not append it
                new_start = min(new_start, interval[0])
                break
            res.append(interval)

        for i in range(i, len(intervals)):
            if new_stop < intervals[i][0]:
                i -= 1
                break
        if i >= 0:
            new_stop = max(new_stop, intervals[i][1])
        res.append([new_start, new_stop])
        res.extend(intervals[i + 1 :])
        return res
