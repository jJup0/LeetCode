"""
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from
nums. The remaining 2 * n elements will be divided into two equal parts:
- The first n elements belonging to the first part and their sum is sum_first.
- The next n elements belonging to the second part and their sum is sum_second.

The difference in sums of the two parts is denoted as sum_first - sum_second.
- For example, if sum_first = 3 and sum_second = 2, their difference is 1.
- Similarly, if sum_first = 2 and sum_second = 3, their difference is -1.

Return the minimum difference possible between the sums of the two parts after
the removal of n elements.

Constraints:
- nums.length == 3 * n
- 1 <= n <= 10^5
- 1 <= nums[i] <= 10^5
"""

import heapq
from collections import Counter
from typing import (
    Iterator,
    MutableSet,
    Protocol,
    Sequence,
    TypeVar,
    cast,
    runtime_checkable,
)

from sortedcontainers.sortedlist import SortedList


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        """
        Split nums in two halves and take the largest of the right half and
        smallest of left half. At each iteration move the split index one to
        the right, i.e. move one number from left to right side. If number
        was one of the n-largest remaining on the right side, replace it
        with the next largest. If number is in the top n smallest numbers in
        the left, remove the largest and add it to the left active subset.

        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """
        n = len(nums) // 3
        # keep max heap of current active numbers in left sum
        left_side = [-num for num in nums[:n]]
        heapq.heapify(left_side)
        right_side = sorted(nums[n:])
        # n-largest numbers in right half, and remaining numbers
        inactive_right_side = SortedList(right_side[:n])
        active_right_side = SortedList(right_side[n:])

        # current sum of left and right halves
        l_sum = -sum(left_side)
        r_sum = sum(active_right_side)
        res = l_sum - r_sum
        # iterate through possible "split indexes"
        for i in range(n, 2 * n):
            num_to_move_to_left = nums[i]
            if num_to_move_to_left in active_right_side:
                # number is in n-largest of right side, need to replace it
                active_right_side.remove(num_to_move_to_left)
                next_biggest_unused = inactive_right_side.pop()
                active_right_side.add(next_biggest_unused)
                r_sum += -num_to_move_to_left + next_biggest_unused
            else:
                inactive_right_side.remove(num_to_move_to_left)

            biggest_left_side = -left_side[0]
            if num_to_move_to_left < biggest_left_side:
                # replace current number with largest on left side
                heapq.heapreplace(left_side, -num_to_move_to_left)
                l_sum += -biggest_left_side + num_to_move_to_left

            # update res with current score
            res = min(res, l_sum - r_sum)
        return res


def test():
    res = Solution().minimumDifference([7, 9, 5, 8, 1, 3])
    assert res == 1, res


def test2():
    # fmt: off
    res = Solution().minimumDifference([16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23])
    # fmt: on
    assert res == -14, res


def test3():
    res = Solution().minimumDifference([7, 9, 5, 8, 1, 3])
    assert res == 1, res


test()
test2()
test3()
