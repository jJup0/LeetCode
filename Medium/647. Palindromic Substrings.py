"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.countSubstrings_v2(s)

    def countSubstrings_v2(self, s: str) -> int:
        """
        O(n) / O(n)     time / space complexity
        """
        # buffer s to avoid out of bounds checks, results in O(n) extra space
        s = "\u0000" + s + "\u0001"
        end_idx = len(s) - 1

        # left and right pointer in string from where to build palindrome
        l = r = 1

        # result variable
        num_palindromes = 0

        while r < end_idx:
            # Step 1. find identical consecutive characters
            starting_char = s[l]
            while s[r] == starting_char:
                r += 1
            # palindromes for repeating identical characters is ((r-l) choose 2)
            num_palindromes += ((r - l) * (r - l + 1)) // 2

            # Step 2. use this sequence of identical characters as the center to build palindromes
            # r points to the first character != s[l]
            ext_left = l - 1
            ext_right = r
            # while adding characters on either side still makes substring a palindrome add to
            # result variable and increase range of j and k
            while s[ext_left] == s[ext_right]:
                num_palindromes += 1
                ext_left -= 1
                ext_right += 1

            # new starting position (l) is first index that was not same character as previous ones
            l = r

        return num_palindromes

    def countSubstrings_v1(self, s: str) -> int:
        """
        Has quadratic runtime for strings where are characters are the same.
        """
        n = len(s)
        buffered_s = "\u0000" + s + "\u0001"
        res = 1
        prev = buffered_s[1]
        for seed in range(2, n + 1):
            c = buffered_s[seed]

            # odd length palidromes
            diff = 1
            while buffered_s[seed - diff] == buffered_s[seed + diff]:
                diff += 1
            res += diff

            # even length palidromes
            if c == prev:
                diff = 1
                while buffered_s[seed - diff - 1] == buffered_s[seed + diff]:
                    diff += 1
                res += diff

            prev = c

        return res
