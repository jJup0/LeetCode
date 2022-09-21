from typing import List


class Solution:
    """
    You are given an integer array nums and an array queries where queries[i] = [val_i, index_i].
    For each query i, first, apply nums[indexi] = nums[indexi] + vali, then print the sum of the
    even values of nums.
    Return an integer array answer where answer[i] is the answer to the ith query.
    Constraints:
        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        1 <= queries.length <= 10^4
        -10^4 <= vali <= 10^4
        0 <= indexi < nums.length
    """

    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        O(n) / O(1)     time / (extra) space complexity
        """
        # sum up all even numbers
        even = sum((n * (not (n & 1))) for n in nums)

        # reserving space for result is twice as fast with given test cases
        res = [0]*len(queries)

        for i, (val, idx) in enumerate(queries):
            # note previous value at index, and check parity of previous and new value
            prev = nums[idx]
            prev_odd = prev & 1
            new_sum_odd = ((prev + val) & 1)

            if prev_odd:
                # if previously odd and now even, add new value to even sum
                if (not new_sum_odd):
                    even += prev + val
            else:
                if new_sum_odd:
                    # if previously even and now odd, remove previous value from even sum
                    even -= prev
                else:
                    # if still even, add difference (val) to even sum
                    even += val

            # update value
            nums[idx] += val

            # add new even sum to result
            res[i] = even

        return res
