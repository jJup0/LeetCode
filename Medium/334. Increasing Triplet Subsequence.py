from typing import List


class Solution:
    """
    Given an integer array nums, return true if there exists a triple of indices (i, j, k) such
    that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

    Constraints:
        1 <= nums.length <= 5 * 10^5
        -2^31 <= nums[i] <= 2^31 - 1
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Store smallest possible values for nums[i] and nums[j], and return when a bigger value
        than nums[j] is encountered.
        O(n) / O(1)     time / space complexity
        """

        # set first and second value to maxint
        first = second = (1 << 31) - 1

        for num in nums:
            # update first if num is smaller than first, else if its smaller than second update
            # second, else found a number that is bigger than both first and second so return true

            # "first" could be a value with an index that comes after "second", but this does not
            # matter, because as long as "second" is set (!= max_int) and a value bigger than
            # second was found, there must have been a value smaller than second previously
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True

        return False
