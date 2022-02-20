class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        def helper(curl, remainingl):
            for i in range(len(remainingl)):
                num = remainingl.pop(i)
                templ = curl + [num]
                if len(templ) == n:
                    retList.append(templ)
                    break
                else:
                    helper(templ, remainingl[:])
                    remainingl.insert(i, num)
        n = len(nums)
        retList = []
        helper([], nums)
        return retList
