"""
You are given an array nums of distinct integers.

In one operation, you can swap any two adjacent elements in the array.

An arrangement of the array is considered valid if the parity of adjacent
elements alternates, meaning every pair of neighboring elements consists of one
even and one odd number.

Return the minimum number of adjacent swaps required to transform nums into any
valid arrangement.

If it is impossible to rearrange nums such that no two adjacent elements have
the same parity, return -1.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- All elements in nums are distinct.
"""


class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        evens: list[int] = []
        odds: list[int] = []
        for i, num in enumerate(nums):
            if num & 1:
                odds.append(i)
            else:
                evens.append(i)

        if abs(len(odds) - len(evens)) > 1:
            # impossible to make alternating array
            return -1

        # reverse to make easier to pop()
        odds.reverse()
        evens.reverse()

        # try starting with odd and/or even number as first number
        start_with_odd: list[bool] = []
        if len(odds) >= len(evens):
            start_with_odd.append(True)
        if len(odds) <= len(evens):
            start_with_odd.append(False)

        res = len(nums) ** 2
        for next_num_odd in start_with_odd:
            _odds = odds.copy()
            _evens = evens.copy()
            swap_count = 0
            for i in range(len(nums) - 1):
                if next_num_odd != (_odds[-1] < _evens[-1]):
                    # next number has wrong parity, swap it to the current index
                    if next_num_odd:
                        swap_count += _odds[-1] - i
                    else:
                        swap_count += _evens[-1] - i
                # remove number from stack
                if next_num_odd:
                    _odds.pop()
                else:
                    _evens.pop()
                next_num_odd = not next_num_odd
            res = min(res, swap_count)
        return res


def test():
    s = Solution()
    res = s.minSwaps([2, 4, 5, 7])
    real = 1
    assert res == real, res

    assert s.minSwaps([2]) == 0
    assert s.minSwaps([3]) == 0
    assert s.minSwaps([2, 3]) == 0
    assert s.minSwaps([3, 2]) == 0


test()
