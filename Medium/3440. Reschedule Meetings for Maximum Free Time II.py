"""
You are given an integer eventTime denoting the duration of an event. You are
also given two integer arrays startTime and endTime, each of length n.

These represent the start and end times of n non-overlapping meetings that
occur during the event between time t = 0 and time t = eventTime, where the ith
meeting occurs during the time [startTime[i], endTime[i]].

You can reschedule at most one meeting by moving its start time while
maintaining the same duration, such that the meetings remain non-overlapping,
to maximize the longestcontinuous period of free time during the event.

Return the maximum amount of free time possible after rearranging the meetings.

Note that the meetings can not be rescheduled to a time outside the event and
they should remain non-overlapping.

Note:In this version, it is valid for the relative ordering of the meetings to
change after rescheduling one meeting.

Constraints:
- 1 <= eventTime <= 10^9
- n == startTime.length == endTime.length
- 2 <= n <= 10^5
- 0 <= startTime[i] < endTime[i] <= eventTime
- endTime[i] <= startTime[i + 1] where i lies in the range [0, n - 2].
"""

import heapq
import itertools


class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: list[int], endTime: list[int]
    ) -> int:
        """
        Precalculate gaps between events, for each event try to stick it in
        the largest gap that it does not neighbor, if no such gap exists,
        slide it as early (or late, does not matter) as possible without
        changing the order.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """

        events = sorted(zip(startTime, endTime))
        gaps = [events[0][0]]
        gaps.extend(e2[0] - e1[1] for e1, e2 in itertools.pairwise(events))
        gaps.append(eventTime - events[-1][1])

        largest_gaps_idxs = heapq.nlargest(3, [(gap, i) for i, gap in enumerate(gaps)])
        res = 0
        for i, (start, end) in enumerate(events):
            gap_before = gaps[i]
            gap_after = gaps[i + 1]
            # default maximum is sliding to as early as possible without
            # changing order, resulting in the two gaps being merged
            # together (in terms of duration)
            res = max(res, gap_before + gap_after)
            duration = end - start
            for gap_size, gap_idx in largest_gaps_idxs:
                if gap_idx not in (i, i + 1) and duration <= gap_size:
                    res = max(res, gap_before + gap_after + duration)
                    break

        return res
