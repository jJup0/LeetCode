"""
Given an array arr of integers, check if there exist two indices i and j such that:
- i!= j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]

Constraints:
- 2 <= arr.length <= 500
- -10^3 <= arr[i] <= 10^3
"""


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        """
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        prev: set[int] = set()
        for num in arr:
            if num * 2 in prev:
                return True
            if num % 2 == 0 and num / 2 in prev:
                return True
            prev.add(num)
        return False
