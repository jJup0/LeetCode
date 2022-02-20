class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(i, curSum, curList):
            if curSum == target:
                retList.append(curList)
            for j in range(i, self.n):
                val = candidates[j]
                if (nextSum := curSum + val) > target:
                    return
                helper(j, nextSum, curList + [val])

        retList = []
        self.n = len(candidates)
        candidates.sort()
        helper(0, 0, [])
        return retList
