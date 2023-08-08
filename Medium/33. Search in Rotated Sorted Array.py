class Solution:
    """
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown
    pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k],
    nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
    [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target, return
    the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4
    - All values of nums are unique.
    - nums is an ascending array that is possibly rotated.
    - -10^4 <= target <= 10^4
    """

    def search(self, nums: list[int], target: int) -> int:
        """
        At every iteration of the binary search, check in which half the rotation point is.
        Technically do not need to check once nums[l:r] is known to be strictly increasing.

        O(log(n)) / O(1)    time / space complexity
        """

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                # pivot is in second half
                if nums[l] <= target < nums[mid]:
                    # target is in non rotated first half
                    r = mid - 1
                else:
                    # target is in rotated second half
                    l = mid + 1
            else:
                # pivot is in first half
                if nums[mid] < target <= nums[r]:
                    # target is in non rotated second half
                    l = mid + 1
                else:
                    # target is in rotated first half
                    r = mid - 1
        return -1
