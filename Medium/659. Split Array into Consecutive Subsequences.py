from collections import Counter, defaultdict
from typing import List


class Solution:
    """
    You are given an integer array nums that is sorted in non-decreasing order.
    Determine if it is possible to split nums into one or more subsequences such that both of the
    following conditions are true:
    Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more
    than the previous integer).
    All subsequences have a length of 3 or more.
    Return true if you can split nums according to the above conditions, or false otherwise.
    A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).
    Constraints:
        1 <= nums.length <= 10^4
        -1000 <= nums[i] <= 1000
        nums is sorted in non-decreasing order.
    """

    def isPossible(self, nums: List[int]) -> bool:
        """
        WARNING: Makes use of Python 3.7 feature, where dictionairies (so also Counters)
        maintain insertion order when iterating over them.
        Create a Counter of nums, greedily assign values (in increasing order) to the end of
        existing sequences, else start a new one
        O(n) / O(n)     space / time complexity
        """

        # use counter to remaining values which still need to be included in a consecutive increasing sequence
        occurances = Counter(nums)

        # dictionary to track endings/last values of existing consecutive sequences
        endings = Counter()

        # iterate over values in increasing order (Python 3.7 required for correctness)
        for val, occs in occurances.items():
            # first greedily add occurances of current value to the end of existing sequences
            added_to_end = min(endings[val-1], occs)
            endings[val-1] -= added_to_end
            endings[val] += added_to_end
            occs -= added_to_end

            # then create new subsequences with current value as start
            # need to check if occs > 0, otherwise fetching occurances[val + x] creates an key in
            # the Counter, causing dictionary size to change without returning false
            if occs:
                if occurances[val + 1] >= occs and occurances[val+2] >= occs:
                    occurances[val + 1] -= occs
                    occurances[val + 2] -= occs
                    endings[val + 2] += occs
                else:
                    # if there are not enough values val+1 and val+2, return false - at least one
                    # of the occurances of val cannot be assigned a consecutive sequence
                    return False

        # all values have been assigned a sequence
        return True
