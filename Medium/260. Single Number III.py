class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        # xor contains the two single numbers xor'ed together
        # means if a bit in xor is set, only one of the two numbers will have it set at that position

        # this bit hack get the lowest set bit, any will set bit will suffice though
        bit = xor & ~(xor-1)

        # repeat xor process, but this time, separate numbers out by this set bit
        # xor the numbers with the set bit with one another, and the numbers with it cleared with one another
        # the two single numbers CANNOT have this bit both set, so they will be xor'ed separately
        ret1 = ret2 = 0
        for num in nums:
            if num & bit:
                ret1 ^= num
            else:
                ret2 ^= num
        return (ret1, ret2)

        # xor = 0
        # for num in nums:
        #     xor ^= num
        # print(xor, bin(xor))
        # for num in nums:
        #     xor ^= num
        #     print(num, xor, bin(xor))

        # nums.sort()
        # retList = []
        # i = 0
        # while i < len(nums) -  1:
        #     if nums[i] == nums[i+1]:
        #         i += 2
        #     else:
        #         retList.append(nums[i])
        #         if len(retList) == 2:
        #             return retList
        #         i += 1
        # return retList + [nums[-1]]
