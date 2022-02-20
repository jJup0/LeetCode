from typing import List
from collections import Counter, defaultdict
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        A,B,C,D = Counter(A),Counter(B),Counter(C),Counter(D)
        ABsums = defaultdict(int)
        res = 0
        
        for aVal, aCount in A.items():
            for bVal, bCount in B.items():
                ABsums[aVal+bVal] += aCount * bCount
                
        for cVal, cCount in C.items():
            for dVal, dCount in D.items():
                negsum= -(cVal+dVal)
                if negsum in ABsums:
                    res += ABsums[negsum] * cCount * dCount
        return res