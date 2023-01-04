from collections import Counter
from math import ceil


class Solution:
    """
    You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level
    of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

    Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to
    complete all the tasks.

    Constraints:
        1 <= tasks.length <= 10^5
        1 <= tasks[i] <= 10^9
    """

    def minimumRounds(self, tasks: list[int]) -> int:
        # result variable
        rounds = 0

        # iterate through task counts
        for count in Counter(tasks).values():
            # if only one task is availible, it cannot be done
            if count == 1:
                return -1

            # otherwise need ceil(count/3) rounds to finish all tasks
            rounds += ceil(count / 3)

        return rounds
