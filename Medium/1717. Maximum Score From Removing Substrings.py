"""
You are given a string s and two integers x and y. You can perform two types of
operations any number of times.
- Remove substring"ab" and gain x points.
  - For example, when removing"ab" from"cabxbae" it becomes"cxbae".
- Remove substring"ba" and gain y points.
  - For example, when removing"ba" from"cabxbae" it becomes"cabxe".

Return the maximum points you can gain after applying the above operations on s.

Constraints:
- 1 <= s.length <= 10^5
- 1 <= x, y <= 10^4
- s consists of lowercase English letters.
"""

from typing import Iterable


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Greedily perform higher operation first, and then other operation
        O(n) / O(n)     time / space complexity
        """
        self.res = 0

        if x > y:
            reduced_s = self._maximum_gain_greedy(s, "a", "b", x)
            self._maximum_gain_greedy(reduced_s, "b", "a", y)
        else:
            reduced_s = self._maximum_gain_greedy(s, "b", "a", y)
            self._maximum_gain_greedy(reduced_s, "a", "b", x)

        return self.res

    def _maximum_gain_greedy(
        self,
        s: Iterable[str],
        first_letter: str,
        second_letter: str,
        operation_score: int,
    ) -> list[str]:
        """
        Greedily performs operation on s with the string `first_letter + second_letter`
        O(n) / O(n)     time / space complexity
        """
        # pad bottom of character stack with arbitrary letter unequal to a or b
        char_stack: list[str] = ["x"]
        for c in s:
            if c == second_letter and char_stack[-1] == first_letter:
                char_stack.pop()
                self.res += operation_score
            else:
                char_stack.append(c)
        return char_stack
