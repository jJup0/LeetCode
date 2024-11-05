"""
Given two strings s and goal, return true if and only if s can become goal
after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost
position.
- For example, if s ="abcde", then it will be"bcdea" after one shift.

Constraints:
- 1 <= s.length, goal.length <= 100
- s and goal consist of lowercase English letters.
"""


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        if len(s) > len(goal):
            # cover cases like s="aa", goal="a"
            return False
        # searching for s in goal concatenated to itself is like searching with shift
        return s in goal * 2
