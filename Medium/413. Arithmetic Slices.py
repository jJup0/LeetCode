from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # Lists with fewer than 3 elements cannot contain arithmetic sequence,
        # case needed to prevent index out of range error
        if len(nums) < 3:
            return 0
        
        diff = nums[1] - nums[0]        # diff stores current difference in arithmetic sequence
        prev = nums[1]                  # prev stores previous value
        res = 0                         # result
        streak = 2                      # size of current arithmetic subsequence
        # start at third element
        for num in nums[2:]:
            # calculate new difference
            new_diff = num - prev
            if new_diff == diff:
                streak += 1
            else:
                # if new difference is different to old, add amount of 3+ element subsequences of current arithmetic
                # subsequence amount of subsequences are length_of_sequence choose 2 (binomial coefficient),
                # however in this amount included are (n-1) possible subsequences of length 2, (length 0 and 1 not
                # accounted for in "n choose m" formula) so these have to be subtracted
                res += (streak * (streak-1))//2 - (streak - 1)
                diff = new_diff
                # streak resets to 2, because two consecutive numbers always form arithmetic sequence 
                streak = 2
                
            prev = num
        
        return res + (streak * (streak-1))//2 - (streak - 1)


print([1][1])