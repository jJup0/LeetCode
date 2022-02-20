class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []

        def findCombo(biggest, prev, prevsum):
            if len(prev) == k:
                if prevsum == n:
                    retList.append(prev)
                return
            if prevsum > n:
                return
            for i in range(biggest+1, min(10, n - prevsum+1)):
                findCombo(i, prev+[i], prevsum+i)
        retList = []
        findCombo(0, [], 0)
        return retList
