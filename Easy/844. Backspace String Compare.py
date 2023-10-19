"""
Given two strings s and t, return true if they are equal when both are typed into
empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Constraints:
- 1 <= s.length, t.length <= 200
- s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?
"""


class Solution:
    def backspaceCompare(self, s_1: str, s_2: str) -> bool:
        """
        O(n) / O(1)     time / space complexity
        """

        prev_s_idx = len(s_1)
        prev_t_idx = len(s_2)
        # compare strings in reverse, to make working with backspaces easier
        while prev_s_idx or prev_t_idx:
            s_c, prev_s_idx = self._next_char(s_1, prev_s_idx)
            t_c, prev_t_idx = self._next_char(s_2, prev_t_idx)
            # if next characters are different return false
            if s_c != t_c:
                return False
        # if all characters were the same, return true
        return True

    def _next_char(self, string: str, idx: int) -> tuple[str, int]:
        """Gets the next charater of a special encoded string.

        Args:
            string (str): String to get next character of
            idx (int): End index (exclusive) from which to start "searching" from

        Returns:
            tuple[str, int]: A tuple with the next character, and the index with which to call the function the next time
        """

        # keep track of how many '#' were encountered so far
        backspaces = 0
        while idx > 0:
            idx -= 1
            c = string[idx]
            # if the char is a back space, add to count
            if c == "#":
                backspaces += 1
            elif backspaces:
                # else, if there are backspaces left to consume, do so
                backspaces -= 1
            else:
                # else return the character
                return c, idx
        # function was either called with idx=0, or backspaces "deleted" all remaining characters
        return "$", 0
