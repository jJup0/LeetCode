from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        sCounterDict = Counter(s)
        for i in sCounterDict:
            if sCounterDict[i] == 1:
                return s.index(i)
        return -1
