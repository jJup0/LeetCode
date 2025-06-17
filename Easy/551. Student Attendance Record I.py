"""
You are given a string s representing an attendance record for a student where
each character signifies whether the student was absent, late, or present on
that day. The record only contains the following three characters:
-'A': Absent.
-'L': Late.
-'P': Present.

The student is eligible for an attendance award if they meet both of the
following criteria:
- The student was absent ('A' ) for strictly fewer than 2 days total.
- The student was never late ('L' ) for 3 or more consecutive days.

Return true if the student is eligible for an attendance award, or false otherwise.

Constraints:
- 1 <= s.length <= 1000
- s[i] is either'A','L', or'P'.
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1:
            return False
        late_streak = 0
        for c in s:
            if c == "L":
                late_streak += 1
                if late_streak == 3:
                    return False
            else:
                late_streak = 0
        return True
