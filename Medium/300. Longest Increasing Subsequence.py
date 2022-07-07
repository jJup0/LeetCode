class Solution:
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.
    A subsequence is a sequence that can be derived from an array by deleting some or no elements
    without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence
    of the array [0,3,1,6,2,2,7].
    Constraints:
        1 <= nums.length <= 2500
        -10^4 <= nums[i] <= 10^4
    """

    def lengthOfLIS(self, nums):
        """
        O(n * log(n)) / O(n)    time/space complexity
        """
        # result variable
        res = 0

        # tails[i] stores smallest tail of all increasing subsequences with length i+1
        tails = [0] * len(nums)

        for num in nums:
            # binary search, find closest val bigger than num and overwrite
            # if num is biggest so far, will overwrite end of tails list, virtually appending
            lo, hi = 0, res
            while lo < hi:
                mid = (lo + hi) >> 1
                if tails[mid] < num:
                    lo = mid + 1
                else:
                    hi = mid

            # overwrite tails[lo], guaranteed to be smaller
            tails[lo] = num
            res = max(lo + 1, res)

        return res
