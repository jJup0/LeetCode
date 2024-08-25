"""
Given a string n representing an integer, return the closest integer (not
including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

Constraints:
- 1 <= n.length <= 18
- n consists of only digits.
- n does not have leading zeros.
- n is representing an integer in the range [1, 10^18 - 1].
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        For each number there are 4 ways of constructing a closest palindrome candidate, check them all.
        O(len(n)) / O(len(n))   time / space complexity
        """
        int_n = int(n)
        # special case for single digit numbers
        if int_n <= 10:
            return str(int_n - 1)

        candidates: list[str] = []

        # simply simply mirror n
        simple_mirrored = self._gen_mirror(n)
        if simple_mirrored != n:
            candidates.append(simple_mirrored)

        # increment or decrement the middle digit
        inc_dec_power_10 = 10 ** (len(n) // 2)
        candidates.append(self._gen_mirror(str(int_n + inc_dec_power_10)))
        candidates.append(self._gen_mirror(str(int_n - inc_dec_power_10)))

        # closest smallest number consisting of all 9s
        candidates.append("9" * (len(n) - 1))

        # return closest candidate, or smallest when equal distance
        return min(candidates, key=lambda x: ((abs(int(x) - int_n), int(x)), x))

    def _gen_mirror(self, s: str):
        """Generates a palindrome using the first half of the characters in s.
        O(len(s)) time & complexity
        """
        second_half = s[: len(s) // 2][::-1]
        if len(s) & 1:
            return s[: len(s) // 2 + 1] + second_half

        return s[: len(s) // 2] + second_half

    def brute_force_nearest_palindromic(self, n: str):
        """
        Was use to find edge cases for actual nearestPalindromic().
        O(n) / O(1)     time / space complexity
        """
        int_n = int(n)
        lower = int_n - 1
        higher = int_n + 1
        while str(lower) != str(lower)[::-1]:
            lower -= 1
        while str(higher) != str(higher)[::-1]:
            higher += 1

        if higher - int_n < int_n - lower:
            return str(higher)
        return str(lower)
