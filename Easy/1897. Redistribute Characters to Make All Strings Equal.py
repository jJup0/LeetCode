"""
You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a
non-empty string, and move any character from words[i] to any position in
words[j].

Return trueif you can make every string in wordsequal using any number of
operations, and falseotherwise.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.
"""
from collections import Counter


class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        """
        O(total_chars) / O(total_chars)     time / space complexity
        """
        letter_counts = Counter(c for word in words for c in word)
        total_words = len(words)
        for letter_count in letter_counts.values():
            if letter_count % total_words:
                return False
        return True
