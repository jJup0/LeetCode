class Solution:
    def findMaxLength(self, nums: [int]) -> int:
        # prev_sums as {count:index} tracks first occurance of an amount of 1s vs 0s
        prev_sums = {0: -1}
        result, countSum = 0, 0
        for i, num in enumerate(nums):
            # if num is 1 add 1, if num is 0 subtract 1
            countSum += num or -1
            # if current sum has already occurred at index j, then nums[j:i+1] has same amount of 0s and 1s 
            if countSum in prev_sums:
                contiguous_length = i - prev_sums[countSum]
                # if calculated length longer than previous, store it
                if contiguous_length > result:
                    result = contiguous_length
            else:
                # if current sum has never occurred then take note of current index
                prev_sums[countSum] = i
        return result