from typing import List


class Solution:
    """
    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number. Let these two numbers be
    numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
    Return the indices of the two numbers, index1 and index2, added by one as an integer array
    [index1, index2] of length 2.
    The tests are generated such that there is exactly one solution. You may not use the same
    element twice.
    Your solution must use only constant extra space.
    Constraints:
        2 <= numbers.length <= 3 * 10^4
        -1000 <= numbers[i] <= 1000
        numbers is sorted in non-decreasing order.
        -1000 <= target <= 1000
        The tests are generated such that there is exactly one solution.
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # take values from left and right end
        l = 0
        r = len(numbers) - 1
        while l <= r:
            two_sum = numbers[l] + numbers[r]

            # if sum is too low, increase l, to increase next sum
            if two_sum < target:
                l += 1
            elif two_sum > target:
                # if sum to too high, decrease r, to decrease next sum
                r -= 1
            else:
                # target found, +1 as result should be 1-indexed
                return [l+1, r+1]
            
        # constraint states there should always be a pair
        assert(False)
