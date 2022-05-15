from collections import Counter, deque
from typing import List


class Solution:
    """
    Given a collection of numbers, nums, that might contain duplicates,
    return all possible unique permutations in any order.
    Constraints:
        1 <= nums.length <= 8
        -10 <= nums[i] <= 10
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def helper():
            nonlocal permutation
            nonlocal remaining_deque
            nonlocal ret_list
            # if only one item left, create resulting permutation, append to nonlocal result and return
            if len(remaining_deque) == 1:
                ret_list.append(permutation + [remaining_deque[0]])
                return

            # stores the previous number, to avoid duplicate results when constructing permutations
            prevnum = remaining_deque[0] - 1
            # cycle through all remaining items
            for _ in range(len(remaining_deque)):
                # pop one number from the list
                num = remaining_deque.popleft()
                # if it is unequal the previous number, append to the permutation and call recursively, pop from permutation
                if prevnum != num:
                    permutation.append(num)
                    helper()
                    prevnum = num
                    permutation.pop()
                # add the number back on to the end of the deque
                remaining_deque.append(num)

        # results list, appended to in helper()
        permutation = []
        remaining_deque = deque(sorted(nums))
        ret_list = []
        # sort the numbers to avoid duplicate permuations, create a deque for performance reasons
        helper()
        return ret_list

    # version optimized for many duplicate items
    def permuteUniqueWithCounter(self, nums: List[int]) -> List[List[int]]:

        def helper(remaining):
            nonlocal permutation
            nonlocal counter
            nonlocal ret_list

            if remaining == 0:
                ret_list.append(permutation.copy())

            # need to use list() otherwise error stating keys changed during iteration
            # if many unique items, space/time complexity in O(n^2)
            for num in list(counter.keys()):
                # do not use .items(), to lower space complexity
                count = counter[num]
                if count == 1:
                    del counter[num]
                    permutation.append(num)
                    helper(remaining-1)
                    permutation.pop()
                    counter[num] = 1
                else:
                    counter[num] -= 1
                    permutation.append(num)
                    helper(remaining-1)
                    permutation.pop()
                    counter[num] += 1

        permutation = []
        counter = Counter(nums)
        ret_list = []
        helper(len(nums))
        return ret_list


# S = Solution()
# x = S.permuteUniqueWithCounter([1, 1, 2, 2, 2])
# print(x)
