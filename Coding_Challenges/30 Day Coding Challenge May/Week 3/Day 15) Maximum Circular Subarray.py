class Solution:
    def maxSubarraySumCircular(self, A: [int]) -> int:
        max_dp, min_dp = A[:], A[:]
        for i in range(1, len(A)):
            max_dp[i] = (max_dp[i-1] if max_dp[i-1] > 0 else 0) + A[i]
            min_dp[i] = (min_dp[i-1] if min_dp[i-1] < 0 else 0) + A[i]
        max_, min_ = max(max_dp), min(min_dp)
        S = sum(A)
        return max(max_, S-min_) if S != min_ else max_
        # return max of biggest normal subarray and everything - smallest subarray (cyclic subarray)
        # if the entire list is negative (s == min_) then return the largest subarray (=smallest negative item)


class faiollSolution:
    def maxSubarraySumCircular(self, nums: [int]) -> int:
        nums = nums*2
        print(nums)
        best = (-1, -1, -100000000000)
        starti = sumsofar = 0

        for i, num in enumerate(nums):
            if i == starti + (len(nums)//2):
                print(nums[starti:i+1])
                print('preSub: i_', starti, 'i', i, 'sumsofar:', sumsofar)
                sumsofar -= nums[starti]
                starti += 1
                print('preLoop: i_', starti, 'i', i, 'sumsofar:', sumsofar)
                while nums[starti] < 0:
                    sumsofar -= nums[starti]
                    starti += 1
                    print('inLoop: i_', starti, 'i', i, 'sumsofar:', sumsofar)
                print('postLoop: i_', starti, 'i', i, 'sumsofar:', sumsofar)
            sumsofar += num
            print('postcur i_', starti, 'i', i, 'sumsofar:', sumsofar)
            if sumsofar > best[2]:
                best = (starti, i, sumsofar)
                print('best:', best)
            if sumsofar < 0:
                if i > (len(nums)//2):
                    print('neg in second loop')
                    break
                sumsofar = 0
                starti = i
        return best[2]
