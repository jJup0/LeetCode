"""
You are given an integer eventTime denoting the duration of an event, where the
event occurs from time t = 0 to time t = eventTime.

You are also given two integer arrays startTime and endTime, each of length n.
These represent the start and end time of n non-overlapping meetings, where the
ith meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most k meetings by moving their start time while
maintaining the same duration, to maximize the longestcontinuous period of free
time during the event.

The relative order of all the meetings should stay the same and they should
remain non-overlapping.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event.

Constraints:
- 1 <= eventTime <= 10^9
- n == startTime.length == endTime.length
- 2 <= n <= 10^5
- 1 <= k <= n
- 0 <= startTime[i] < endTime[i] <= eventTime
- endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
"""


class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: list[int], endTime: list[int]
    ) -> int:
        """
        Always bunch `k` consecutive events together and make them take
        place as early as possible, check time until next event and update result.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        meetings = sorted(zip(startTime, endTime))
        # start time and duration of current k-block
        k_block_start = 0
        k_block_total_time = sum(end - start for start, end in meetings[:k])
        res = 0
        for i, (next_meeting_start, next_meeting_end) in enumerate(
            meetings[k:], start=k
        ):
            # update result if shifting current k block makest largest gap so far
            res = max(res, next_meeting_start - (k_block_start + k_block_total_time))
            # remove `i-k`th meeting from k-block
            remove_start, remove_end = meetings[i - k]
            k_block_total_time -= remove_end - remove_start
            k_block_start = remove_end
            # add current meeting to k-block
            k_block_total_time += next_meeting_end - next_meeting_start

        # return max of current result and shifting the last k events as
        # early as possible to have a "gap" time until the end of the event
        return max(res, eventTime - (k_block_start + k_block_total_time))
