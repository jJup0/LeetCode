from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # """
    # This is MountainArray's API interface.
    # You should not implement it, or speculate about its implementation
    # """
    class MountainArray:
        def get(self, index: int) -> int:
            ...

        def length(self) -> int:
            ...


class Solution:
    """
    (This problem is an interactive problem.)

    You may recall that an array arr is a mountain array if and only if:
    - arr.length >= 3
    - There exists some i with 0 < i < arr.length - 1 such that:
      - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
      - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

    Given a mountain array mountainArr, return the minimum index such that
    mountainArr.get(index) == target. If such an index does not exist, return -1.

    You cannot access the mountain array directly. You may only access the array
    using a MountainArray interface:
    - MountainArray.get(k) returns the element of the array at index k (0-indexed).
    - MountainArray.length() returns the length of the array.

    Submissions making more than 100 calls to MountainArray.get will be judged
    Wrong Answer. Also, any solutions that attempt to circumvent the judge will
    result in disqualification.

    Constraints:
    - 3 <= mountain_arr.length() <= 10^4
    - 0 <= target <= 10^9
    - 0 <= mountain_arr.get(index) <= 10^9
    """

    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        peek = self._find_peek(mountain_arr)

        # binary search mountain array before peek (increasing array) first
        lo = 0
        hi = peek
        while lo <= hi:
            mid = (lo + hi) >> 1
            mid_val = mountain_arr.get(mid)
            if mid_val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        if mountain_arr.get(lo) == target:
            return lo

        # binary search mountain array after peek (decreasing array)
        lo = peek
        hi = mountain_arr.length() - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            mid_val = mountain_arr.get(mid)
            if mid_val >= target:
                lo = mid + 1
            else:
                hi = mid - 1
        if mountain_arr.get(hi) == target:
            return hi

        # if not found on either side of peek, return -1
        return -1

    def _find_peek(self, mountain_arr: "MountainArray") -> int:
        lo = 0
        hi = mountain_arr.length() - 1
        while lo <= hi:
            mid = (lo + hi) >> 1
            mid_val = mountain_arr.get(mid)
            mid_next_val = mountain_arr.get(mid + 1)
            if mid_val < mid_next_val:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo
