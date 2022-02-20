class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        def helper(cur_i, cur_comb, remainder):
            if remainder == 0:
                retList.append(cur_comb)
                return

            for i in range(cur_i, len(candidates)):
                if candidates[i] > remainder:
                    break
                helper(i, cur_comb + [candidates[i]], remainder - candidates[i])
        
        # to break ealier 
        candidates.sort()
        retList = []
        helper(0, [], target)
        return retList