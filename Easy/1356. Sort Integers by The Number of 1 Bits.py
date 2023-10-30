"""
You are given an integer array arr. Sort the integers in the array in ascending
order by the number of 1's in their binary representation and in case of two or
more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.

Constraints:
- 1 <= arr.length <= 500
- 0 <= arr[i] <= 104
"""


class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key=lambda x: (x.bit_count(), x))
        return arr
