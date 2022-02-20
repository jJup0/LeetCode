class Solution:
    def countBits(self, num: int) -> [int]:
        ogBlock = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
        blen = len(ogBlock)
        retVal = ogBlock[:]
        for x in range(1, int((num//blen)+1)):
            retVal += [num + retVal[x] for num in ogBlock]
        end = -(blen-1-num % blen) if blen-1-num % blen else None
        return retVal[:end]


class notMySolution:
    def countBits(self, num: int) -> [int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & (i-1)] + 1
        return dp
