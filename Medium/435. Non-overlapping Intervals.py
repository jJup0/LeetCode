class Solution:
    """
    Given an array of intervals intervals where intervals[i] = [start_i, end_i], return
    the minimum number of intervals you need to remove to make the rest of the intervals
    non-overlapping.

    Constraints:
    - 1 <= intervals.length <= 10^5
    - intervals[i].length == 2
    - -5 * 10^4 <= start_i < end_i <= 5 * 10^4
    """

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        return self._sort_by_stop_time(intervals)

    def _eraseOverlapIntervals_naive(self, intervals: list[list[int]]) -> int:
        """
        First attempt, sorts by interval start and uses "stack" which is not necessary
        as it always contains exactly one value.
        O(n) / O(1)     time / space complexity
        """
        # sort by start
        intervals.sort(key=lambda interval: interval[0])

        # intervals which are still currently "active"
        # # ~~invariant: values on stack are strictly increasing~~
        # actual invariant: stack always contains one value
        interval_ends_stack: list[int] = []

        # amount of intervals removed
        removed = 0
        for start, stop in intervals:
            # pop off all intervals which end before the current interval starts
            while interval_ends_stack and start >= interval_ends_stack[-1]:
                interval_ends_stack.pop()

            # whether or not the current interval should
            delete_current_interval = False
            # all remaining intervals on the stack overlap with the current interval
            while interval_ends_stack:
                removed += 1
                # keep the lowest possible stop times on the stack; i.e ...
                if interval_ends_stack[-1] >= stop:
                    # ... if the interval in the stack ends after the current interval,
                    # remove the interval from the stack (delete the interval) ...
                    interval_ends_stack.pop()
                else:
                    # ... else delete the current interval
                    delete_current_interval = True
                    break

            # add the current interval to the stack if it should not be deleted
            # invariant: stack is empty at this point
            if not delete_current_interval:
                interval_ends_stack.append(stop)

        return removed

        return intervals_removed

    def _sort_by_stop_time(self, intervals: list[list[int]]) -> int:
        """
        Sort by end time. Iterate through intervals and delete if
        previous interval stops after current interval starts.
        O(n) / O(1)     time / space complexity
        """

        intervals = sorted(intervals, key=lambda x: x[1])
        prev_stop = -1_000_000

        intervals_removed = 0
        for start, stop in intervals:
            if start < prev_stop:
                # intervals overlap, remove the current interval, so do not
                # update prev_stop, as it is lower than current stop
                intervals_removed += 1
            else:
                # intervals do not overlap, update prev_stop
                prev_stop = stop
        return intervals_removed
