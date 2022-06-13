from collections import defaultdict
from typing import List


class Solution:
    """
    You are given an array of positive integers nums and want to erase a subarray containing
    unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
    Return the maximum score you can get by erasing exactly one subarray.
    An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is,
    if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
    Constraints:
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^4
    """

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # last seen mapping for values, default to -1 when not seen yet
        last_seen = defaultdict(lambda: -1)

        # current sum of unique subarray
        running_sum = 0

        # result variable
        res = 0

        # current start index for unique subarray
        start = 0

        for i, val in enumerate(nums):
            # if current value is part of unique subarray,
            if last_seen[val] >= start:
                # update res if running sum is new maximum
                if running_sum > res:
                    res = running_sum

                # subtract all numbers up to last occurance of that number
                new_start = last_seen[val] + 1
                running_sum -= sum(nums[j] for j in range(start, new_start))

                # new start index is last occurance of val + 1
                start = new_start

            # add value to running sum
            running_sum += val

            # update last occurance
            last_seen[val] = i

        # return maximum of previous greatest running sum and current
        return max(res, running_sum)
