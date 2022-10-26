from typing import List


class Solution:
    """
    Given an integer array nums and an integer k, return true if nums has a continuous subarray of
    size at least two whose elements sum up to a multiple of k, or false otherwise.

    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a
    multiple of k.
    
    Constraints:
        1 <= nums.length <= 10^5
        0 <= nums[i] <= 10^9
        0 <= sum(nums[i]) <= 2^31 - 1
        1 <= k <= 2^31 - 1
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Calculate running sums of nums, if there is a duplicate entry at index i and j, then the
        subarray with a summing to a multiple of k will be nums[i+1:j+1]
        O(n) / O(n)     time / space complexity
        """
        # current running sum modulo k
        curr_sum = 0

        # set of running sums
        running_sums_set = set([0])

        # previous number in nums, only important if zero or not
        prev = -1
        for num in nums:
            # take modulo if num, important if num is multiple of k
            num %= k
            # add num to the running sum
            curr_sum = (curr_sum + num) % k

            # if num is not a multiple of k, otherwise subarray "identified" would have length 1
            if num:
                # if it has been seen in running sums so far, return true
                if (curr_sum in running_sums_set):
                    return True
                # else add if to the set
                running_sums_set.add(curr_sum)
            elif not prev:
                # if the previous number was also a multiple of k, then the subarray is nums[i-1:i+1]
                return True

            prev = num

        # if no duplicate entries in running sum, return false
        return False
