"""
Run-length encoding is a string compression method that works by replacing
consecutive identical characters (repeated 2 or more times) with the
concatenation of the character and the number marking the count of the
characters (length of the run). For example, to compress the string "aabccc" we
replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string
becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at mostk characters from
s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting
at most k characters.

Constraints:
- 1 <= s.length <= 100
- 0 <= k <= s.length
- s contains only lowercase English letters.
"""
from functools import cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        O(n^2 * k) / O(n^2 * k)     time / space complexity
        """

        @cache
        def length_opt_del(
            start_idx: int, last_char: str, last_count: int, deletions_remaining: int
        ) -> int:
            """
            Returns minimum length of s[start_idx:] when run length encoded after deleting
            deletions_remaining characters, if the last `last_count` characters are `last_char`.
            """
            nonlocal s

            # if whole string iterated through, no letter to be removed, therefore RLE length is 0
            if start_idx == n:
                return 0

            curr_char = s[start_idx]

            if curr_char == last_char:
                # If charcter is the same as last, always keep it, deletion is
                # handled in "else" case when a new character is first encountered

                # keeping the character increases RLE length by one if it is the:
                # - second: a -> a2,
                # - tenth: a9 -> a10
                # - or hundredth character: a99 -> a100
                extra_length_for_no_delete = (
                    last_count == 1 or last_count == 9 or last_count == 99
                )

                return extra_length_for_no_delete + length_opt_del(
                    start_idx + 1, last_char, last_count + 1, deletions_remaining
                )
            else:
                # compare minimum length of sting if current char is kept vs deleted and return minimum
                res_for_keep = 1 + length_opt_del(
                    start_idx + 1, s[start_idx], 1, deletions_remaining
                )
                if deletions_remaining:
                    res_for_del = length_opt_del(
                        start_idx + 1, last_char, last_count, deletions_remaining - 1
                    )
                    return min(res_for_keep, res_for_del)
                return res_for_keep

        n = len(s)
        return length_opt_del(0, "", 0, k)
