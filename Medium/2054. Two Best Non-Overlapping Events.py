"""
You are given a 0-indexed 2D integer array of events where
events[i] = [startTime_i, endTime_i, value_i]. The ith event starts at
startTime_i _and ends at endTime_i, and if you attend this event, you will
receive a value of value_i. You can choose at mosttwonon-overlapping events to
attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend
two events where one of them starts and the other ends at the same time. More
specifically, if you attend an event with end time t, the next event must start
at or after t + 1.

Constraints:
- 2 <= events.length <= 10^5
- events[i].length == 3
- 1 <= startTime_i <= endTime_i <= 10^9
- 1 <= value_i <= 10^6
"""

import bisect


class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        return self.maxTwoEvents2(events)

    def maxTwoEvents1(self, events: list[list[int]]) -> int:
        """
        Sort events by start time, for each index `i` pre calculate the
        largest value events[i:], then for each event bisect events array
        to get the smallest compatible index and use the precomputed max
        value for events including and after that event.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        events.sort()
        n = len(events)

        # prefix max values, last index remains empty
        max_values: list[int] = [0] * (len(events) + 1)
        curr_max_value = 0
        # iterate through events in reverse order to easily find
        # maximum value of events[i:].
        for i, (_, _, val) in enumerate(reversed(events), start=1):
            if val > curr_max_value:
                curr_max_value = val
            max_values[n - i] = curr_max_value

        # for each event, bisect for the index of the earliest
        # compatible event, and use the value of max_values[idx]
        # to calculate the best pair value for that event
        best_pair_value = 0
        for _start, end, val in events:
            lowest_compatible_idx = bisect.bisect_left(
                events, end + 1, key=lambda x: x[0]
            )
            best_pair_value = max(
                best_pair_value, val + max_values[lowest_compatible_idx]
            )

        return best_pair_value

    def maxTwoEvents2(self, events: list[list[int]]) -> int:
        """
        Reverse approach, sort by end time, then bisect previous events' start time.
        Faster for leetcode tests, presumably because list size for bisection is
        much smaller and entries are integers and not tuples.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        events.sort(key=lambda x: x[1])

        # track largest value events in the past and their index
        prev_max_values = [0]
        prev_max_values_end_times = [-1]

        max_pair_value = 0
        for start, end, value in events:
            # index of previous event in max_weights
            idx = bisect.bisect_right(prev_max_values_end_times, start - 1) - 1
            max_pair_value = max(max_pair_value, value + prev_max_values[idx])

            # if new heighest value, append to the max values lists
            if value > prev_max_values[-1]:
                prev_max_values.append(value)
                prev_max_values_end_times.append(end)

        return max_pair_value
