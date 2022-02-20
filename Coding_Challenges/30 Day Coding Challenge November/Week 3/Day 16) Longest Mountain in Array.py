class Solution:
    def longestMountain(self, A):
        res = up = down = 0                     # result, current upwards streak, current downwards streak
        for i in range(1, len(A)):              # go through all nums, starting with second
            bigger = A[i - 1] < A[i]            # stores if curr is bigger than prev
            same = A[i - 1] == A[i]             # stores if curr is same as prev
            if down and (bigger or same):       # if currently heading down, but current number is larger or same
                up = down = 0                   # -> reset
            up += bigger                        # increase up-streak if bigger
            down += not (bigger or same)        # increase down-streak if smaller
            if up and down:                     # if there if a mountain is in session
                res = max(res, up + down + 1)   # update max
        return res                              # return biggest mountain
