"""
Given an integer array arr, remove a subarray (can be empty) from arr such that
the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

Constraints:
- 1 <= arr.length <= 10^5
- 0 <= arr[i] <= 10^9
"""

"""
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.
"""


class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        """
        Complexity:
            Time: O(n)
            Space: O(1)
        """
        l = self._find_increasing_length_start(arr)
        if l == len(arr) - 1:
            return 0
        r = self._find_increasing_length_end(arr)

        # res by default is to use only start or only end
        res = min(len(arr) - l - 1, r)
        # try all index pairs where cutting out arr[i+1:j] results in
        # a non-decreasing array
        for i in range(l + 1):
            while r < len(arr) and arr[i] > arr[r]:
                r += 1
            if r == len(arr):
                break
            res = min(res, r - i - 1)
        return res

    def _find_increasing_length_start(self, arr: list[int]):
        prev = arr[0] - 1
        l = 0
        for l, num in enumerate(arr):
            if prev > num:
                l -= 1
                break
            prev = num
        return l

    def _find_increasing_length_end(self, arr: list[int]):
        prev = arr[-1] + 1
        j = len(arr) - 1
        for j in range(len(arr) - 1, -1, -1):
            num = arr[j]
            if prev < num:
                j += 1
                break
            prev = num
        return j

    def brute_force(self, arr: list[int]) -> int:
        # used to fuzz test actual solution, O(n^3*log(n)) complexity
        for remove_len in range(len(arr)):
            for start in range(len(arr) - remove_len + 1):
                cut_arr = arr[:start] + arr[start + remove_len :]
                if cut_arr == sorted(cut_arr):
                    return remove_len
        return -1
