"""
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length, pref.length <= 100
- words[i] and pref consist of lowercase English letters.
"""


class Solution:
    def prefixCount(self, words: list[str], prefix: str) -> int:
        """
        Complexity:
            n := len(words), m := len(prefix)
            Time: O(n * m)
            Space: O(1)
        """
        return sum(1 for word in words if word.startswith(prefix))
