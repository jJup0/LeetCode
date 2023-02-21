class Solution:
    """
    You are given a sorted array consisting of only integers where every element appears exactly
    twice, except for one element which appears exactly once.

    Return the single element that appears only once.

    Your solution must run in O(log n) time and O(1) space.

    Constraints:
        1 <= nums.length <= 10^5
        0 <= nums[i] <= 10^5
    """

    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        "Normal" binary search problem. If even middle value and its successor are the same value
        then single value is between mid + 2 and high, else between low and mid.
        """

        low = 0
        high = len(nums) - 1
        # maintain loop invariant that the single value is in nums[lo:hi+1]
        while low < high:
            mid = (low + high) >> 1

            # make sure mid is even
            if mid & 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # single value is at least at index mid + 2
                low = mid + 2
            else:
                # single value is at most at mid
                high = mid

        return nums[low]
