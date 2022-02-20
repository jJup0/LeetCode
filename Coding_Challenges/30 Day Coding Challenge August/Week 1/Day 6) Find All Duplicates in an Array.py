class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        retSet = set()
        hadSet = set()
        for num in nums:
            if num in hadSet:
                retSet.add(num)
            else:
                hadSet.add(num)
        return retSet
