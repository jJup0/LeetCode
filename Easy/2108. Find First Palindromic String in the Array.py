"""
Given an array of strings words, return the first palindromic string in the
array. If there is no such string, return an empty string"".

A string is palindromic if it reads the same forward and backward.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists only of lowercase English letters.
"""


class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        """
        O(sum(len(w) for w in words)) / O(max(len(w)) for w in words)   time / space complexity
        """
        for word in words:
            if word == word[::-1]:
                return word
        return ""
