class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # problem can be simpilified down to house robber problem: leetcode.com/problems/house-robber/
        # whereby each row of houses is just consecutive numbers in the array, and the value of 
        # each house is the sum of numbers with the same value
        
        # sort numbers to have consecutive numbers next to each other
        nums.sort()
        # ensures consecutive "streak" ends at the end
        nums.append(-1)
        # virtual "houses to rob" list
        consecutives = [nums[0]]
        prev = nums[0]
        res = 0
        for num in nums[1:]:
            # if number is the same as previous, then increment last entry by number
            if num == prev:
                consecutives[-1] += num
            elif num == prev + 1:
                # if one higher then add new "house" with value of num
                consecutives.append(num)
            else:
                # if the streak of consecutive house is broken: apply house robber algorithm
                # new curr_dp is calculated by taking the maximum value of taking the previous dp (2 houses
                # ago) and stealing from current house, or stealing from last house
                prev_dp, curr_dp = 0, 0
                for num in consecutives:
                    prev_dp, curr_dp = curr_dp, max(prev_dp + num, curr_dp) 
                res += curr_dp
                # reset houses list to one house with value of num                
                consecutives = [num]
        
            prev = num
        return res