class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mods = [0]*60
        for c in time:
            mods[c % 60] += 1

        res = 0
        for i, c in enumerate(mods[1:30], start=1):
            if c:
                res += c * mods[60-i]
        return res + (mods[0]*(mods[0]-1))//2 + (mods[30]*(mods[30]-1))//2
