class Solution:
    """
    An array arr a mountain if the following properties hold:
    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
      - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
      - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Given a mountain array arr, return the index i such that arr[0] < arr[1] < ...
    < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

    You must solve it in O(log(arr.length)) time complexity.

    Constraints:
    - 3 <= arr.length <= 10^5
    - 0 <= arr[i] <= 10^6
    - arr is guaranteed to be a mountain array.
    """

    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        """
        Regular binary search with condition `arr[mid] < arr[mid + 1]`.
        O(log(n)) / O(1)    time / space complexity
        """
        lo = 1
        hi = len(arr) - 2
        while lo < hi:
            mid = (lo + hi) >> 1
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
