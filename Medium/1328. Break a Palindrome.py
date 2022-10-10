class Solution:
    """
    Given a palindromic string of lowercase English letters palindrome, replace exactly one
    character with any lowercase English letter so that the resulting string is not a palindrome
    and that it is the lexicographically smallest one possible.

    Return the resulting string. If there is no way to replace a character to make it not a
    palindrome, return an empty string.

    A string a is lexicographically smaller than a string b (of the same length) if in the first
    position where a and b differ, a has a character strictly smaller than the corresponding
    character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first
    position they differ is at the fourth character, and 'c' is smaller than 'd'.

    Constraints:
        1 <= palindrome.length <= 1000
        palindrome consists of only lowercase English letters.
    """

    def breakPalindrome(self, palindrome: str) -> str:
        """
        O(n) / O(1)     time / (extra) space complexity
        """
        n = len(palindrome)
        # if string has at most one character, it will always be a palidrome
        if n <= 1:
            return ""

        # find first index i in palindrome which can be replaced with 'a', which break the
        # palindrome, only search first half of the word including excluding middle letter
        replace_idx = 0
        for replace_idx in range(n // 2 + 1):
            if (palindrome[replace_idx] > 'a'):
                break
        
        # if all letters were 'a', or middle letter is the only one unequal to 'a', then 
        # replace_idx is last index, and replace letter is 'b', else replace letter is 'a'
        replace_letter = 'a'
        if replace_idx == n//2:
            replace_idx = n - 1
            replace_letter = 'b'

        return f"{palindrome[:replace_idx]}{replace_letter}{palindrome[replace_idx+1:]}"
