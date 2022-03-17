from typing import List


class Solution:
    # constraint: popped is permutation of pushed
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        i_pop = i_push = 0
        # constraint: 0 <= pushed[i] <= 1000, -1 acts as dummy entry when check top of stack for equality
        stack = [-1]
        for i_pop in range(len(popped)):

            to_pop = popped[i_pop]
            # push items onto stack until top of stack is equal to item to pop
            while i_push < len(pushed) and stack[-1] != to_pop:
                stack.append(pushed[i_push])
                i_push += 1

            # check again if top of stack is equal
            if stack[-1] == to_pop:
                stack.pop()
            else:
                # else pushed entries have been exhausted and return false
                # assert i_push == len(pushed)
                return False

        # popped list exhausted meaning pushed and popped represent stack sequence
        # assert stack == [-1]
        return True
