def nopenextPermutation(self, nums: [int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) == 2:
        nums[0], nums[1] = nums[1], nums[0]
        return
    retVal = nums.copy()
    i = len(nums) - 1
    biggestVal = 0
    while i > 0:
        if nums[i] >= biggestVal:
            biggestVal = nums[i]
        else:
            retVal = nums[:i] + nums[:i-1:-1]
            nums[:] = retVal
            # print('done')
            return
        i -= 1
    if nums and nums[0] < biggestVal:
        # print('rev')
        i = len(nums)-1
        firstnum = nums[0]
        temp = []
        while i > 0:
            if nums[i] > firstnum:
                temp.append(nums.pop(i))
                print(temp)
                break
            i -= 1
        nums.sort()
        temp += nums
        nums[:] = temp
        return
    # print('sort')
    nums.sort()


class Solution:
    def nextPermutation(self, nums: [int]) -> None:
        i = len(nums) - 1
        biggestVal = 0
        while i >= 0:
            if nums[i] >= biggestVal:
                biggestVal = nums[i]
            else:
                retVal = nums[:i]
                firstnum = nums[i]
                j = len(nums)-1
                while j > i:
                    if nums[j] > firstnum:
                        retVal.append(nums.pop(j))
                        break
                    j -= 1
                temp = nums[i:]
                temp.sort()
                nums[:] = retVal + temp
                return
            i -= 1
        nums.sort()
