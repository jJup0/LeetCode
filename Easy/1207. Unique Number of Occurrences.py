"""
Given an array of integers arr, return true if the number of occurrences of each
value in the array is unique or false otherwise.

Constraints:
- 1 <= arr.length <= 1000
- -1000 <= arr[i] <= 1000
"""


from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        """
        O(n) / O(n)     time / space complexity
        """
        counter = Counter(arr)
        unique_occurances = set(counter.values())
        return len(counter) == len(unique_occurances)
