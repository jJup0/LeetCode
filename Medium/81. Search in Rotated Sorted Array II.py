class Solution:
    """
    There is an integer array nums sorted in non-decreasing order (not
    necessarily with distinct values).

    Before being passed to your function, nums is rotated at an unknown
    pivot index k (0 <= k < nums.length) such that the resulting array
    is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
    (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at
    pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

    Given the array nums after the rotation and an integer target, return
    true if target is in nums, or false if it is not in nums.

    You must decrease the overall operation steps as much as possible.

    Constraints:
    - 1 <= nums.length <= 5000
    - -10^4 <= nums[i] <= 10^4
    - nums is guaranteed to be rotated at some pivot.
    - -10^4 <= target <= 10^4
    """

    def search(self, nums: list[int], target: int) -> int:
        """
        Worst case scenario we have something like [0,0,0,..., 1, 0, 0...] in
        which case we can gain no speed up by binary search and depending on
        luck, every element needs to be checked, so we cannot do better than
        O(n) time complexity.
        O(n) / O(1)     time / space complexity
        """
        return target in nums

    def actual_binary_search(self, nums: list[int], target: int) -> bool:
        """
        Binary search. Find pivot by incrementing left index until nums[left] != nums[mid].
        O(n) / O(1)     time / space complexity
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            # Check if the target is found
            if nums[mid] == target:
                return True

            # if nums[left] == nums[mid] it is impossible to determine where
            # the pivot is, so increment left
            while left < mid and nums[left] == nums[mid]:
                left += 1
            # either left == mid, in which case all numbers between the original
            # left and mid were the same (therfore no pivot between original left
            # and mid), or nums[left] != nums[mid] and so we can figure out where
            # the pivot is

            # same as seaching in array without duplicates
            if nums[left] <= nums[mid]:
                # pivot is in second half
                if nums[left] <= target < nums[mid]:
                    # target is in non rotated first half
                    right = mid - 1
                else:
                    # target is in rotated second half
                    left = mid + 1
            else:
                # pivot is in first half
                if nums[mid] < target <= nums[right]:
                    # target is in non rotated second half
                    left = mid + 1
                else:
                    # target is in rotated first half
                    right = mid - 1

        return False
