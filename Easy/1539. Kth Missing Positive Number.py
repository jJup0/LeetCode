class Solution:
    """
    Given an array arr of positive integers sorted in a strictly increasing order,
    and an integer k.

    Return the kth positive integer that is missing from this array.

    Constraints:
        1 <= arr.length <= 1000
        1 <= arr[i] <= 1000
        1 <= k <= 1000
        arr[i] < arr[j] for 1 <= i < j <= arr.length
    """

    def findKthPositive(self, arr: list[int], k: int) -> int:
        """
        Binary seach for index in arr that comes either right before
        or right after the kth missing number.
        O(log(n)) / O(1)    time / space complexity
        """
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) >> 1
            # amount of values missing up until mid is value at mid - mid
            missing = arr[mid] - mid
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        # val_at_low = arr[min(len(arr)-1, low)]
        # missing = val_at_low - low
        # return val_at_low + k - missing
        return low + k  # equivalent to above
