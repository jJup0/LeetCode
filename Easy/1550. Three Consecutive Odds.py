"""
Given an integer array arr, return true if there are three consecutive odd
numbers in the array. Otherwise, return false.
Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000
"""


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        """
        O(n) / O(1)     time / space
        """
        odd_streak = 0
        for num in arr:
            if num & 1:
                odd_streak += 1
                if odd_streak == 3:
                    return True
            else:
                odd_streak = 0
        return False
