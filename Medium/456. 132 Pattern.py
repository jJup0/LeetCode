from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []                              # stack to track decreasing vals for num_k candidates
        num_k = float('-inf')                   # last (middle value) number
        for num in reversed(nums):

            if num < num_k:                     # num = num_i
                return True

            while stack and stack[-1] < num:    # kickout all numbers so far that are smaller, store last one
                num_k = stack.pop()             # contains biggest number smaller than num_j candidate = num_k
            stack.append(num)                   # append num_j candidate, biggest number lies at bottom of stack

        return False
