from typing import List


class Solution:
    """
    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
    that each unique element appears only once. The relative order of the elements should be kept
    the same.

    Since it is impossible to change the length of the array in some languages, you must instead
    have the result be placed in the first part of the array nums. More formally, if there are k
    elements after removing the duplicates, then the first k elements of nums should hold the final
    result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array
    in-place with O(1) extra memory.

    Custom Judge:

    The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
    If all assertions pass, then your solution will be accepted.

    Constraints:
        1 <= nums.length <= 3 * 10^4
        -100 <= nums[i] <= 100
        nums is sorted in non-decreasing order.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        O(n) / O(1)     time / space complexity
        """
        
        # previous number
        prev = None
        
        # total amount of unique values so far, also index for where next unique value will be
        # placed
        res = 0
        
        for num in nums:
            # if num is unique, or first of its value replace previous duplicate and update res
            if num != prev:
                nums[res] = num
                res += 1
            prev = num
        return res
