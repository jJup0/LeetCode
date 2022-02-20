# from collections import Counter
# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         res = 0
#         if k == 0:
#             c = Counter(nums)
#             for count in c.values():
#                 res += count > 1
#             return res

#         nums = sorted(set(nums))
#         print(nums)
#         i = 0
#         j = bisect.bisect_left(nums, nums[0]+k)
#         while j < len(nums):
#             if nums[i] + k < nums[j]:
#                 i += 1
#             elif nums[i] + k > nums[j]:
#                 j += 1
#             else:
#                 i += 1
#                 j += 1
#                 res += 1
#         return res
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        res = 0
        if k == 0:
            for count in c.values():
                res += count > 1
        else:
            for c_key in c:
                res += c_key + k in c
        return res
