"""
Given an array of integers arr and an integer k. Find the least number of
unique integers after removing exactlyk elements.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^9
- 0 <= k <= arr.length
"""

from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        """
        Remove least common numbers first.
        O(n * log(n)) / O(n)    time / space complexity
        """
        counter = Counter(arr)
        remaining_unique = len(counter)
        for _, count in sorted(counter.items(), key=lambda x: x[1]):
            if count > k:
                break
            k -= count
            remaining_unique -= 1
        return remaining_unique
