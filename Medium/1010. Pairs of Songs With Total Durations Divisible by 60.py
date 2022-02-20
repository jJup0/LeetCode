from typing import List
import math

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        timeMod60 = [0] * 60
        for t in time:
            timeMod60[t%60] += 1
        res = math.comb(timeMod60[0],2)
        res += math.comb(timeMod60[30],2)
        for i in range(1, 30):
            res += timeMod60[i] * timeMod60[60-i]
        return res
            