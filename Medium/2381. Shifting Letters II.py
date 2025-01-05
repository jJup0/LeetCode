"""
You are given a string s of lowercase English letters and a 2D integer array
shifts where shifts[i] = [start_i, end_i, direction_i]. For every i, shift the
characters in s from the index start_i to the index end_i (inclusive) forward
if direction_i = 1, or shift the characters backward if direction_i = 0.

Shifting a character forward means replacing it with the next letter in the
alphabet (wrapping around so that'z' becomes'a' ). Similarly, shifting a
character backward means replacing it with the previous letter in the alphabet
(wrapping around so that'a' becomes'z' ).

Return the final string after all such shifts to s are applied.

Constraints:
- 1 <= s.length, shifts.length <= 5 * 10^4
- shifts[i].length == 3
- 0 <= start_i <= end_i < s.length
- 0 <= direction_i <= 1
- s consists of lowercase English letters.
"""

import itertools


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        shift_counts = self._get_letter_shifts(len(s), shifts)
        return "".join(
            self._shift_character(c, shift_by) for c, shift_by in zip(s, shift_counts)
        )

    def _get_letter_shifts(self, n: int, shifts: list[list[int]]):
        # deltas[i] = amount of extra shift to apply to all letters starting from index i
        shift_deltas = [0] * (n + 1)
        for i, j, direction in shifts:
            d = 1 if direction else -1
            shift_deltas[i] += d
            shift_deltas[j + 1] += -d

        return itertools.accumulate(shift_deltas)

    def _shift_character(self, char: str, shift_by: int) -> str:
        # normalize characters so 'a' == 0;
        normalized_0_char = ord(char) - ord("a")
        # shift
        shifted_0_char = (normalized_0_char + shift_by) % 26
        # transform back to letter
        return chr(shifted_0_char + ord("a"))
