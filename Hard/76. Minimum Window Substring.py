"""
Given two strings s and t of lengths m and n respectively, return the minimum
window substring of s such that every character in t (including duplicates) is
included in the window. If there is no such substring, return the empty string
"".

The testcases will be generated such that the answer is unique.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Find window with lowest upper index including all characters,
        then increasing lower index as long as all characters are included.
        Then again increase upper index until all characters are included and repeat.
        n := len(s)
        O(n) / O(n)     time / space complexity
        """
        n = len(s)
        # remaining characters and their count in t to cover by s substring,
        # values may be decremented below 0
        remaining_chars = Counter(t)
        # total count of remaining characters in t to cover by s substring
        remaining_count = len(t)

        # left and right index of shortest substring
        best_l = -1
        best_r = n

        # `l` and `r` are the left and right index of current subtring in s
        l = 0
        for r, right_char in enumerate(s):
            # shift right index of substring until all characters in t are covered, or end of s is reached
            if right_char not in remaining_chars:
                continue
            # if s[r] is a relevant character, decrement remaining_count if the remaining
            # count needed for s[r] is greater than 0
            remaining_count -= remaining_chars[right_char] > 0
            # decrement characters of s[r] needed
            remaining_chars[right_char] -= 1
            if remaining_count:
                # if there are characters still left to cover, increment r
                continue

            # increment r (overidden at next iteration), so that s[l:r] contains the full substring
            r += 1

            # shift left index until a character would be missing
            for l in range(l, r):
                left_char = s[l]
                if left_char not in remaining_chars:
                    continue
                remaining_chars[left_char] += 1
                if remaining_chars[left_char] > 0:
                    # if remaining chars greater than zero, then cannot remove s[l], would have to increase r
                    # s[l] to be removed from substring so remaining count back up to 1
                    remaining_count = 1
                    # so check if s[l:r+1] is shortest substring so far covering and update accordingly
                    if (r - l) < (best_r - best_l):
                        best_l = l
                        best_r = r
                    break
            l += 1

        if best_l == -1:
            return ""
        return s[best_l:best_r]
