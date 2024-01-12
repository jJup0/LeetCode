"""
You are given a string s of even length. Split this string into two halves of
equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i',
'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and
lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Constraints:
- 2 <= s.length <= 1000
- s.length is even.
- s consists of uppercase and lowercase letters.
"""
from collections import Counter


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        """
        O(n) / O(n)     time / space complexity
        """
        vowels = "aeiouAEIOU"
        half_len = len(s) // 2
        half1 = Counter(s[:half_len])
        half2 = Counter(s[half_len:])

        vowels1 = sum(half1[vowel] for vowel in vowels)
        vowels2 = sum(half2[vowel] for vowel in vowels)
        return vowels1 == vowels2
