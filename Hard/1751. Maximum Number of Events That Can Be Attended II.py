import bisect
from functools import cache


class Solution:
    """
    You are given an array of events where events[i] = [startDayi, endDayi, valuei].
    The ith event starts at startDayi and ends at endDayi, and if you attend this
    event, you will receive a value of valuei. You are also given an integer k
    which represents the maximum number of events you can attend.

    You can only attend one event at a time. If you choose to attend an event,
    you must attend the entire event. Note that the end day is inclusive: that
    is, you cannot attend two events where one of them starts and the other
    ends on the same day.

    Return the maximum sum of values that you can receive by attending events.

    Constraints:
    - 1 <= k <= events.length
    - 1 <= k * events.length <= 10^6
    - 1 <= startDayi <= endDayi <= 10^9
    - 1 <= valuei <= 10^6
    """

    def maxValue(self, events: list[list[int]], k: int) -> int:
        E_END_IDX = 1

        # sort events by end day, to quickly be able to find next previously-occuring
        # event when "choosing" to visit an event
        events.sort(key=lambda x: x[E_END_IDX])
        # keep end days in separate list for binary search
        events_ends = [e[E_END_IDX] for e in events]

        @cache
        def find_best(curr_event_idx: int, picks_remaining: int) -> int:
            """
            Finds the maximum value of visiting upto picks_remaining events
            from events[:curr_event_idx + 1].
            """
            nonlocal events, events_ends
            # curr_event_idx < 0 is true when an event was taken with no
            # other previously occuring event availible
            if curr_event_idx < 0 or picks_remaining == 0:
                return 0

            curr_e_start, _, curr_e_val = events[curr_event_idx]

            # max value for not visiting the current/last event
            do_not_take_curr = find_best(curr_event_idx - 1, picks_remaining)

            # find the next possible previously-occuring event index by binary
            # searching current events start in list of event ends. bisect_left
            # and subtract 1 to get the "latest" compatible event
            next_compatible_event_idx = (
                bisect.bisect_left(events_ends, curr_e_start) - 1
            )

            # maximum value for visiting the current event =
            #   current event value
            #   + maximum value for events[:next_compatible_event_idx] and picks_remaining-1
            take_curr = (
                find_best(next_compatible_event_idx, picks_remaining - 1) + curr_e_val
            )
            # return maximum value of either strategy
            return max(do_not_take_curr, take_curr)

        # find maximum value for any choice of events with k picks remaining
        return find_best(len(events) - 1, k)
