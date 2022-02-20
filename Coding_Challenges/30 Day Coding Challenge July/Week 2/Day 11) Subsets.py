class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        # def createSubsets(curList, remaining):
        #     for i in range(len(remaining)-1, -1, -1):
        #         num = remaining.pop(i)
        #         if curList and num < curList[-1]:
        #             return
        #         templ = curList + [num]
        #         retSet.add(tuple(templ))
        #         createSubsets(templ, remaining[:])
        #         remaining.insert(i, num)
        # retSet = {tuple()}
        # createSubsets([], sorted(nums))
        # return retSet
        retList = [[]]
        for num in nums:
            retList += [prevSubset + [num] for prevSubset in retList]
        return retList
