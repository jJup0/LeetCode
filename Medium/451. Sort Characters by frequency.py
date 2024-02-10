"""
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s consists of uppercase and lowercase English letters and digits.
"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        cs = Counter(s)
        elems = sorted(cs.items(), key=lambda char_count: char_count[1], reverse=True)
        return "".join(c * count for count, c in elems)
