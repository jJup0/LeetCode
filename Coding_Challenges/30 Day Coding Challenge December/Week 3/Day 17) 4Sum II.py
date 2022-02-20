from collections import Counter, defaultdict


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        #         twoSum_1 = Counter()
        #         twoSum_2 = Counter()
        #         for a in A:
        #             for b in B:
        #                 twoSum_1[a+b] += 1
        #         for d in D:
        #             for c in C:
        #                 twoSum_2[c+d] += 1

        #         return sum(count * twoSum_2[-val] for val, count in twoSum_1.items())

        A, B, C, D = Counter(A), Counter(B), Counter(C), Counter(D)
        ABsums = defaultdict(int)
        res = 0

        for aVal, aCount in A.items():
            for bVal, bCount in B.items():
                ABsums[aVal+bVal] += aCount * bCount

        for cVal, cCount in C.items():
            for dVal, dCount in D.items():
                negsum = -(cVal+dVal)
                if negsum in ABsums:
                    res += ABsums[negsum] * cCount * dCount
        return res
        # return sum(ABsums[-(cVal+dVal)] * cCount * dCount for cVal, cCount in C.items() for dVal, dCount in D.items())
