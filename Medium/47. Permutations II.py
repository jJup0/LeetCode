class Solution:
    def permuteUnique(self, nums: [int]) -> [[int]]:
        def helper(curl, remainingl):
            prevnum = None
            for i in range(len(remainingl)):
                num = remainingl.pop(i)
                templ = curl + [num]
                if len(templ) == n:
                    retList.append(templ)
                    break
                if prevnum != num:
                    helper(templ, remainingl[:])
                    prevnum = num
                remainingl.insert(i, num)

        n = len(nums)
        retList = []
        helper([], sorted(nums))
        return retList



