"""
Given a string array words, return an array of all characters that show up in
all strings within the words (including duplicates). You may return the answer
in any order.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 100
- words[i] consists of lowercase English letters.
"""

import operator
from collections import Counter
from functools import reduce


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        """
        O(n) / O(n)     time / space complexity
        """
        return reduce(operator.and_, map(Counter, words)).elements()
