"""
You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For
example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f"
are special.

Return the length of the longest special substring of s which occurs at least
thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

Constraints:
- 3 <= s.length <= 50
- s consists of only lowercase English letters.
"""


class Solution:
    def maximumLength(self, s: str) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        letter_to_count_to_occs: dict[str, list[int]] = {
            chr(_ord): [0] for _ord in range(ord("a"), ord("z") + 1)
        }
        prev = s[0]
        prev_streak = 0
        for c in s:
            if c == prev:
                prev_streak += 1
            else:
                self._streak_break(prev_streak, letter_to_count_to_occs[prev])
                prev = c
                prev_streak = 1
        self._streak_break(prev_streak, letter_to_count_to_occs[prev])

        res = -1
        for streak_to_occs in letter_to_count_to_occs.values():
            for streak, occs in enumerate(streak_to_occs):
                if occs >= 3 and streak > res:
                    res = streak
        return res

    def _streak_break(self, streak: int, count_to_occs: list[int]):
        for i in range(1, streak + 1):
            if i == len(count_to_occs):
                count_to_occs.append(streak - i + 1)
            else:
                count_to_occs[i] += streak - i + 1
