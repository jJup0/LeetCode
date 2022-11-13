from typing import List


class Solution:
    """
    Given an input string s, reverse the order of the words.

    A word is defined as a sequence of non-space characters. The words in s will be separated by at
    least one space.

    Return a string of the words in reverse order concatenated by a single space.

    Note that s may contain leading or trailing spaces or multiple spaces between two words. The
    returned string should only have a single space separating the words. Do not include any extra
    spaces.

    Constraints:
        1 <= s.length <= 10^4
        s contains English letters (upper-case and lower-case), digits, and spaces ' '.
        There is at least one word in s.
    """

    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    def followUp(self, s: List[str]):
        # Follow-up: If the string data type is mutable in your language, can you solve it in-place
        # with O(1) extra space?
        def reverse_word(start, stop):
            half_word_len = ((stop - start) // 2)
            for j in range(half_word_len + 1):
                s[start + j], s[stop - j] = s[stop - j], s[start + j]
        
        first_char_idx = 0
        for i in range(len(s)):
            if s[i] == ' ':
                reverse_word(first_char_idx, i - 1)
                first_char_idx = i + 1

        reverse_word(first_char_idx, len(s) - 1)

        # remore duplicate space
        last_free_idx = 1
        for i in range(1, len(s)):
            if s[i] != ' ' or s[i - 1] != ' ':
                s[last_free_idx] = s[i]
                last_free_idx += 1
        
        return s[:last_free_idx]
