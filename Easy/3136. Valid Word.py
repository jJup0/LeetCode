"""
A word is considered valid if:
- It contains a minimum of 3 characters.
- It contains only digits (0-9), and English letters (uppercase and lowercase).
- It includes at least one vowel.
- It includes at least one consonant.

You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:
-'a','e','i','o','u', and their uppercases are vowels.
- A consonant is an English letter that is not a vowel.

Constraints:
- 1 <= word.length <= 20
- word consists of English uppercase and lowercase letters, digits,'@','#', and'$'.
"""


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        if not word.isalnum():
            return False
        vowels = "AEIOUaeiou"
        has_vowel = has_consonant = False
        for char in word:
            if char in vowels:
                has_vowel = True
            elif not char.isnumeric():
                has_consonant = True
        return has_vowel and has_consonant
