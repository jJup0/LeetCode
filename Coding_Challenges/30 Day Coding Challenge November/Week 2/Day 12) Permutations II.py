class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def createPerm(prev, i):
            if i == n:
                res.append(tuple(prev))
            for num in nums.keys():
                if nums[num]:
                    nums[num] -= 1
                    prev[i] = num
                    createPerm(prev, i+1)
                    nums[num] += 1

        n = len(nums)
        nums = Counter(nums)
        res = []
        createPerm([0]*n, 0)
        return res
