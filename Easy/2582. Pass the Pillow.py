"""
There are n people standing in a line labeled from 1 to n. The first person in
the line is holding a pillow initially. Every second, the person holding the
pillow passes it to the next person standing in the line. Once the pillow
reaches the end of the line, the direction changes, and people continue passing
the pillow in the opposite direction.
- For example, once the pillow reaches the nth person they pass it to the
  n - 1th person, then to the n - 2th person and so on.

Given the two positive integers n and time, return the index of the person
holding the pillow after time seconds.

Constraints:
- 2 <= n <= 1000
- 1 <= time <= 1000
"""


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """
        O(1) / O(1)     time / space complexity
        """
        steps_for_full_loop = 2 * (n - 1)
        # skip all steps that result in starting back at first person
        time %= steps_for_full_loop
        if time < n:
            # if less time than total people remaining,
            # just take time steps and add 1, since 1-indexed
            return time + 1
        # else subtract steps remaining after reaching the end from the total_people-1,
        # add 1 since 1-indexed
        # ((n-1) - (time - (n - 1))) + 1 =
        return steps_for_full_loop - time + 1
