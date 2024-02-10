"""
Given an array of strings strs, group the anagrams together. You can return the answer in any
order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

from collections import defaultdict
from typing import Any


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        O(n * representation_method) / O(n)     time / space complexity
        """
        anagram_dict: dict[Any, list[str]] = defaultdict(list)
        for string in strs:
            anagram_representation = self._anagram_representation_linear(string)
            # add current string to its respective list of anagrams
            anagram_dict[anagram_representation].append(string)
        return list(anagram_dict.values())

    def _anagram_representation_sort(self, s: str):
        """
        Very simple, all anagrams are the same when sorted by their character
        O(n * log(n)) / O(n)    time / space complexity
        """
        return "".join(sorted(s))

    def _anagram_representation_linear(self, s: str):
        """
        O(n) / O(n)    time / space complexity
        """
        ord_a = ord("a")
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord_a] += 1
        return bytes(counts)
