from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # m = nums1.length, n = nums2.length
        # runtime: O(m + n)

        n = len(nums)
        decreasingStack = [float('inf')]
        idxsStack = [-1]
        ret = [-1] * n

        for i in range(2*n):
            num = nums[i % n]

            while num > decreasingStack[-1]:
                decreasingStack.pop()
                idx = idxsStack.pop()
                ret[idx] = num
            if i < n:
                decreasingStack.append(num)
                idxsStack.append(i)

        return ret

    def nextGreaterElements_old_withTuple(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # tracks current decreasing numbers
        decreasingStack = [(-1, float('inf'))]
        # tracks nextGreatest for nums
        nextGreatest = dict(zip(enumerate(nums), [-1]*len(nums)))

        for i in range(2*n):
            num = nums[i % n]

            while num > decreasingStack[-1][1]:
                j, val = decreasingStack.pop()
                nextGreatest[(j, val)] = num
            if i < n:
                decreasingStack.append((i, num))

        return [nextGreatest[(i, x)] for i, x in enumerate(nums)]     # returns generator, not list

    def nextGreaterElements_stolenAndImproved(self, nums: List[int]) -> List[int]:
        # stole this, because runtimes inconsitent and I thought my solution wasnt good
        n = len(nums)
        n_dec = n-1
        nums.reverse()
        stack = nums.copy()
        ret = [-1]*n
        for i, num in enumerate(nums):
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                ret[n_dec-i] = stack[-1]
            stack.append(num)
        return ret
