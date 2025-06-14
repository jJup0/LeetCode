"""
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

Constraints:
- 1 <= words.length <= 50
- 1 <= words[i].length <= 50
- x is a lowercase English letter.
- words[i] consists only of lowercase English letters.
"""


class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [i for i, word in enumerate(words) if x in word]
