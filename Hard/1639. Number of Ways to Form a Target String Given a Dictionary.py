"""
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:
- target should be formed from left to right.
- To form the ith character (0-indexed) of target, you can choose the kth
  character of the jth string in words if target[i] = words[j][k].
- Once you use the kth character of the jth string of words, you can no longer
  use the xth character of any string in words where x <= k. In other words, all
  characters to the left of or at index k become unusuable for every string.
- Repeat the process until you form the string target.

Notice that you can use multiple characters from the same string in words
provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be
too large, return it modulo 10^9 + 7.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 1000
- All strings in words have the same length.
- 1 <= target.length <= 1000
- words[i] and target contain only lowercase English letters.
"""

from collections import Counter
from functools import cache


class Solution:
    MODULUS = 10**9 + 7

    def numWays(self, words: list[str], target: str) -> int:
        """
        n := len(target)
        m := len(words[0])
        w := len(words)
        Complexity:
            Time: O(w * m + n * m)
            Space: O(n * m)
        """
        self.word_len = len(words[0])
        self.target_len = len(target)
        self.target = target
        if self.target_len > self.word_len:
            return 0

        self.idx_to_char_counts: list[Counter[str]] = [
            Counter(chars_at_i) for chars_at_i in zip(*words)
        ]

        # return self._search1(0, 0, 0)
        # return self._search2(self.target_len - 1, self.word_len)
        return self._search3(0, 0)

    def _search1(
        self, current_idx: int, lowest_allowed_idx: int, curr_count: int
    ) -> int:
        """
        Exceeds time limit.
        Complexity:
            Time: O(n^m)
            Space: O(n)
        """
        if current_idx == len(self.target):
            return curr_count % self.MODULUS
        curr_char = self.target[current_idx]

        res = 0
        for i in range(
            lowest_allowed_idx, self.word_len - len(self.target) + current_idx + 1
        ):
            char_count = self.idx_to_char_counts[i][curr_char]
            if not char_count:
                continue
            res += self._search1(current_idx + 1, i + 1, curr_count * char_count)
            res %= self.MODULUS
        return res

    @cache
    def _search2(self, current_idx: int, highest_allowed_idx: int) -> int:
        """
        Completes tests within time limit.

        Complexity:
            Time: O(n * m^2)
            Space: O(n * m)
        """
        curr_char = self.target[current_idx]
        if current_idx == 0:
            return sum(
                self.idx_to_char_counts[i][curr_char]
                for i in range(highest_allowed_idx)
            )
        res = 0
        for i in range(current_idx, highest_allowed_idx):
            count = self.idx_to_char_counts[i][curr_char]
            if not count:
                continue
            res = (res + self._search2(current_idx - 1, i) * count) % self.MODULUS
        return res

    @cache
    def _search3(self, wi: int, ti: int) -> int:
        """
        Complexity:
            Time: O(n * m)
            Space: O(n * m)
        """
        if ti == len(self.target):
            return 1
        if self.word_len - wi < len(self.target) - ti:
            return 0

        count = self.idx_to_char_counts[wi][self.target[ti]]
        return (
            count * self._search3(wi + 1, ti + 1) + self._search3(wi + 1, ti)
        ) % self.MODULUS
