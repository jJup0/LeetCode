from typing import List


class Solution:
    """
    Given an array of n integers nums, a 132 pattern is a subsequence of three
    integers nums[i], nums[j] and nums[k] such that i < j < k and
    nums[i] < nums[k] < nums[j].

    Return true if there is a 132 pattern in nums, otherwise, return false.

    Constraints:
    - n == nums.length
    - 1 <= n <= 2 * 10^5
    - -10^9 <= nums[i] <= 10^9
    """

    def find132pattern(self, nums: List[int]) -> bool:
        # go through list in reverse order, keep stack of all values that have
        # been bigger than biggest value so far, as potential future candidates
        # for being nums[k] in the 132 pattern. top of stack is lowest number,
        # increasing from there.
        stack: list[int] = []

        # value to store hightest nums[k] possible (second highest number while going in reverse order)
        nums_k = float("-inf")
        for num in reversed(nums):
            # if num is smaller than nums_k, num is nums[i] candidate and return True
            if num < nums_k:
                return True

            # if num is larger thatn largest nums[j] candidate so far, virtually set
            # num as nums[j], and update nums_k to be the largest number smaller than num
            while stack and stack[-1] < num:
                nums_k = stack.pop()

            # append num (current nums[j] candidate) to stack,
            # it is potential future nums[k] candidate
            stack.append(num)

        return False
