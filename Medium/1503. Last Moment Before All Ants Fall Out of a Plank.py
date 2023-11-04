"""
We have a wooden plank of the length n units. Some ants are walking on the
plank, each ant moves with a speed of 1 unit per second. Some of the ants
move to the left, the other move to the right.

When two ants moving in two different directions meet at some point, they
change their directions and continue moving again. Assume changing directions
does not take any additional time.

When an ant reaches one end of the plank at a time t, it falls out of the
plank immediately.

Given an integer n and two integer arrays left and right, the positions of
the ants moving to the left and the right, return the moment when the last
ant(s) fall out of the plank.

Constraints:
- 1 <= n <= 104
- 0 <= left.length <= n + 1
- 0 <= left[i] <= n
- 0 <= right.length <= n + 1
- 0 <= right[i] <= n
- 1 <= left.length + right.length <= n + 1
- All values of left and right are unique, and each value can appear only in
  one of the two arrays.
"""


class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        """
        Ant collisions have no effect. Assuming that identities of ants do not
        matter, when two ants collide the next state is the same as if they
        walked passed each other.
        O(n) / O(1)     time / space complexity
        """
        time_for_left_ants = max(left, default=0)
        time_for_right_ants = n - min(right, default=n)
        return max(time_for_left_ants, time_for_right_ants)
