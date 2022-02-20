class Solution:
    def combinationSum2(self, candidates: [int], target: int) -> [[int]]:
        def helper(cur_i, curCandList, remainder):
            if remainder == 0:
                retSet.add(tuple(curCandList))
                return

            for i in range(cur_i, len(candidates)):
                if candidates[i] > remainder:
                    break
                helper(i+1, curCandList+[candidates[i]], remainder-candidates[i])

        candidates.sort()
        retSet = set()
        helper(0, [], target)
        return retSet
