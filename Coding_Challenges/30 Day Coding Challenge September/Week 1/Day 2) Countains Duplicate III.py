class Solution:
    def containsNearbyAlmostDuplicate(self, nums: [int], k: int, t: int) -> bool:
        # numsDict = defaultdict(set)
        # len_nums = len(nums)
        # for i, num in enumerate(nums):
        #     numsDict[num].add(i)
        # nums = sorted(numsDict.keys())
        # for i in range(len(nums)):
        #     j = i
        #     while j < len(nums) and nums[j] - nums[i] <= t:
        #         for i_index in numsDict[nums[i]]:
        #             for j_index in numsDict[nums[j]]:
        #                 if 0 < abs(i_index - j_index) <= k:
        #                     return True
        #         j += 1
        # return False
        if t == 0 and len(nums) == len(set(nums)):
            return False

        for i, num in enumerate(nums):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(num - nums[j]) <= t:
                    return True

        return False
