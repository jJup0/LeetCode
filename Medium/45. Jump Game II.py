class Solution:
    def jump(self, nums: List[int]) -> int:
        lo = 0          # lower bound for currently jumpable inclusive
        hi = 1          # higher bound for currently jumpable exclusive
        count = 0       # return value
        n = len(nums)
        while hi < n:
            # select jump which goes furthest, respecting starting position
            maxJ = max(jump + i for i, jump in enumerate(nums[lo:hi], start=lo + 1))
            # set current high as new low, since anything before hi does not need to be recalculated
            lo = hi
            # set furthest jump high as new high
            hi = maxJ
            count += 1

        return count


#         # slow
#         def dfs(idx, steps):
#             if steps > dp[idx]:
#                 return
#             if idx == ndec:
#                 dp[idx] = steps
#                 return

#             dp[idx] = steps
#             steps += 1
#             for i in range(min(ndec-idx, nums[idx]), 0, -1):
#                 dfs(idx + i, steps)

#         n = len(nums)
#         ndec = n-1
#         dp = [n] * n
#         dfs(0, 0)
#         print(dp)
#         return dp[-1]
