"""
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [start_i, end_i]
means that a meeting will be held during the half-closed time interval
[start_i, end_i). All the values of start_i are unique.

Meetings are allocated to rooms in the following manner:

1. Each meeting will take place in the unused room with the lowest number.
2. If there are no available rooms, the meeting will be delayed until a room becomes
   free. The delayed meeting should have the same duration as the original meeting.

Return the number of the room that held the most meetings. If there are
multiple rooms, return the room with the lowest number.

A half-closed interval[a, b) is the interval between a and b including a and not
including b.

Constraints:
- 1 <= n <= 100
- 1 <= meetings.length <= 10^5
- meetings[i].length == 2
- 0 <= start_i < end_i <= 5 * 10^5
- All the values of start_i are unique.
"""

import heapq


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        """
        O(m * log(n)) / O(n)    time / space complexity
        """
        # min-heap where booked_rooms[i] = (meeting_end, room_nr)
        booked_rooms: list[tuple[int, int]] = []
        # min-heap of rooms which are currently free
        free_rooms = [i for i in range(n)]

        # meetings_held[i] = the amount of meetings held in room i so far
        meetings_held = [0] * n

        # sort meetings by starting time
        meetings.sort()
        for start, stop in meetings:
            # "finish" meetings of booked rooms with ending times before the current meeting starts
            while booked_rooms and booked_rooms[0][0] <= start:
                _, room_nr = heapq.heappop(booked_rooms)
                heapq.heappush(free_rooms, room_nr)

            if free_rooms:
                # if there are free rooms, take the room with the smallest number
                room_nr = heapq.heappop(free_rooms)
            else:
                # else get the meeting which finishes next
                # if two rooms finish at the same time then the room with the
                # number will be popped from the heap
                earliest_start, room_nr = heapq.heappop(booked_rooms)
                # add delay to the meeting while maintaining the duration
                delay = earliest_start - start
                start = earliest_start
                stop += delay

            # note that a meeting was held in the room and push the room to the heap of booked rooms
            meetings_held[room_nr] += 1
            heapq.heappush(booked_rooms, (stop, room_nr))

        # temporary helper array to find room with highest usage,
        # and lowest room number for tie breakers
        count_negated_room_number = [
            (count, -room_nr) for room_nr, count in enumerate(meetings_held)
        ]
        return -max(count_negated_room_number)[1]
