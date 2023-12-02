"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars
(each character can only be used once).

Return the sum of lengths of all good strings in words.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length, chars.length <= 100
- words[i] and chars consist of lowercase English letters.
"""
from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        char_dict = Counter(chars)
        res = 0
        for word in words:
            if Counter(word) <= char_dict:
                res += len(word)
        return res
