from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # m = nums1.length, n = nums2.length
        # runtime: O(m + n)

        # tracks current decreasing numbers
        decreasingStack = [float('inf')]
#       # nextGreatest = dict(zip(nums1, [-1]*len(nums1)))      # tag_1
        # tracks nextGreatest for nums2
        nextGreatest = {}

        for num in nums2:
            while num > decreasingStack[-1]:
                val = decreasingStack.pop()
                nextGreatest[val] = num

#           # if num in nextGreatest:   # tag_1
            decreasingStack.append(num)

        return (nextGreatest.get(x, -1) for x in nums1)     # returns generator, not list


#         # m = nums1.length, n = nums2.length
#         # runtime: O(m * log(m) + n)

#         stack = []
#         ret = [-1]*len(nums1)
#         nums1_idxs = dict(zip(nums1, range(len(nums1))))
#         for num in nums2:
#             if num in nums1_idxs:
#                 heapq.heappush(stack, num)
#             while stack and num > stack[0]:
#                 ret[nums1_idxs[heapq.heappop(stack)]] = num
#         return ret
