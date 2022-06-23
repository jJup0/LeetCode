import heapq
from typing import List


class Solution:
    """
    There are n different online courses numbered from 1 to n. You are given an array courses
    where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken
    continuously for durationi days and must be finished before or on lastDay_i.
    You will start on the 1st day and you cannot take two or more courses simultaneously.
    Return the maximum number of courses that you can take.
    Constraints:
        1 <= courses.length <= 10^4
        1 <= duration_i, lastDay_i <= 10^4
    """

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        Time complexity due to sorting, and pushing/replacing on maxheap up to n-times
        O(n * log(n)) time, O(n) space
        """
        # sort courses by end date, to greedily add courses
        courses.sort(key=lambda x: x[1])

        # amount of days filled with courses so far
        days_used = 0

        # result variable
        res = 0

        # max-heap for longest courses taken so far (uses negated day count)
        # initialize with impossible value of -1 days
        largest = [1]

        # go through courses, end date ascending
        for dur, end in courses:
            # if there is enough time to additionally take the current course, take it
            if end >= days_used + dur:
                # one more course is taken
                res += 1
                # days are used up
                days_used += dur
                # push the course duration to the max-heap (push -dur for max-heap property)
                heapq.heappush(largest, -dur)
            elif dur < -largest[0]:
                # if the course is shorter than the longest course that was going to be
                # take so far, replace this course with the previous course
                negated_prev_largest_duration = heapq.heapreplace(largest, -dur)
                # update days used by subtracting days of longest course, and adding days
                # of current course
                days_used += negated_prev_largest_duration + dur

        return res
