"""
An attendance record for a student can be represented as a string where each
character signifies whether the student was absent, late, or present on that
day. The record only contains the following three characters:
-'A': Absent.
-'L': Late.
-'P': Present.

Any student is eligible for an attendance award if they meet both of the
following criteria:
- The student was absent ('A' ) for strictly fewer than 2 days total.
- The student was never late ('L' ) for 3 or more consecutive days.

Given an integer n, return the number of possible attendance records of length
n that make a student eligible for an attendance award. The answer may be very
large, so return it modulo 10^9 + 7.

Constraints:
- 1 <= n <= 10^5
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        MOD = 10**9 + 7
        # track the different ways to have an attendance record
        # absent_once[i] = number of attendance records where the last i attendances
        #                  were late, with at least one absence
        # analogous for `never_absent`
        absent_once = [0, 0, 0]
        never_absent = [1, 0, 0]

        for _ in range(n):
            absent_once = [
                # latest attendance is "P" from student who was previously absent once,
                # or "A" from stundent who was never absent
                (sum(absent_once) + sum(never_absent)) % MOD,
                # latest attendance is "L" from student who was absent once
                absent_once[0],
                absent_once[1],
            ]
            never_absent = [
                # latest attendance is "P" from student who was never absent
                sum(never_absent) % MOD,
                # latest attendance is "L" from student who was never absent
                never_absent[0],
                never_absent[1],
            ]

        return (sum(absent_once) + sum(never_absent)) % MOD
