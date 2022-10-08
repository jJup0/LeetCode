import bisect
from collections import deque


class MyCalendarThree:

    """
    A k-booking happens when k events have some non-empty intersection (i.e., there is some time
    that is common to all k events.)
    You are given some events [start, end), after each given event, return an integer k
    representing the maximum k-booking between all the previous events.
    Implement the MyCalendarThree class:
    MyCalendarThree() Initializes the object.
    int book(int start, int end) Returns an integer k representing the largest integer such that
    there exists a k-booking in the calendar.

    Constraints:
        0 <= start < end <= 10^9
        At most 400 calls will be made to book.
    """

    def __init__(self):
        self.starts = []
        self.ends = []
        self.k = 0

    def book(self, start: int, end: int) -> int:
        # insert start and end point into lists
        bisect.insort(self.starts, start)
        bisect.insort(self.ends, end)

        # "finished" amount of bookings have already ended before current event starts
        finished = bisect.bisect(self.ends, start)

        # "last_new" is index in self.starts so that all events up until that index have started
        # before current event ends
        last_new = bisect.bisect(self.starts, end)

        # currently overlapping booking endings
        active = deque()

        # iterate through bookings which are active during current event
        for i in range(finished, last_new):
            # bookings ending before starting date of current iteration removed from active pool
            while active and active[0] <= self.starts[i]:
                active.popleft()

            # append booking to active pool
            active.append(self.ends[i])

            # if amount of active bookings is higher than max, update k
            if (newk := len(active)) > self.k:
                self.k = newk

        return self.k


class MyCalendarThree_original:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> int:
        start_pair = start, 1
        end_pair = end, -1

        start_idx = bisect.bisect(self.events, start_pair)
        end_idx = bisect.bisect(self.events, end_pair)

        temp = self.events[:start_idx]
        temp.append(start_pair)
        temp.extend(self.events[start_idx:end_idx])
        temp.append(end_pair)
        temp.extend(self.events[end_idx:])
        self.events = temp

        # can be optimized so that max only needs to search [start_idx:end_idx]
        # & memorizing last result
        curr = res = 0
        for _, val in self.events:
            curr += val
            if curr > res:
                res = curr

        return res
