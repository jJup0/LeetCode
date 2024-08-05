"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string
present in arr. If there are fewer than k distinct strings, return an empty
string"".

Note that the strings are considered in the order in which they appear in the array.

Constraints:
- 1 <= k <= arr.length <= 1000
- 1 <= arr[i].length <= 5
- arr[i] consists of lowercase English letters.
"""

from collections import Counter


class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        """
        O(n) / O(n)     time / space complexity
        """
        uniques = 0
        # use ordered property of dicts (python 3.6+)
        for string, count in Counter(arr).items():
            if count == 1:
                uniques += 1
                if uniques == k:
                    return string
        return ""
