"""
You are given two strings start and target, both of length n. Each string
consists only of the characters'L','R', and'_' where:
- The characters'L' and'R' represent pieces, where a piece'L' can move to the
  left only if there is a blank space directly to its left, and a piece'R' can move
  to the right only if there is a blank space directly to its right.
- The character'_' represents a blank space that can be occupied by any of
  the'L' or'R' pieces.

Return true if it is possible to obtain the string target by moving the pieces
of the string start any number of times. Otherwise, return false.

Constraints:
- n == start.length == target.length
- 1 <= n <= 10^5
- start and target consist of the characters'L','R', and'_'.
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        self.start = start
        self.start_i = 0
        n = len(start)
        for target_i, char in enumerate(target):
            if char == "_":
                continue
            if char == "L":
                if not self._ensure_blank_until(target_i):
                    return False
                if not self._find_next_char("L", n - 1):
                    return False
            elif char == "R":
                if not self._find_next_char("R", target_i):
                    return False
        return self._ensure_blank_until(n)

    def _ensure_blank_until(self, idx_limit: int) -> bool:
        """
        Increments `self.start_i` returning True if start[self.start_i] == "_"
        for all self.start_i up until `idx_limit`, else False.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        while self.start_i < idx_limit:
            if self.start[self.start_i] != "_":
                return False
            self.start_i += 1
        return True

    def _find_next_char(self, char: str, idx_limit: int) -> bool:
        """
        Increments self.start_i until `char` is encountered, at most up
        until `idx_limit`. Returns True if the character is found,
        without encountering the opposite character first.
        `self.start_i` will be incremented to the index after the first
        encounter of char or idx_limit + 1, if not character is found.

        Complexity:
            Time: O(n)
            Space: O(1)
        """
        while self.start_i <= idx_limit and self.start[self.start_i] != char:
            if self.start[self.start_i] != "_":
                # opposite letter encountered which is in the way of trying to move
                return False
            self.start_i += 1
        if self.start_i > idx_limit:
            # character not found
            return False
        self.start_i += 1
        return True
