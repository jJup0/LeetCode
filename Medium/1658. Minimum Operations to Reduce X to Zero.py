from typing import List


class Solution:
    """
    You are given an integer array nums and an integer x. In one operation, you can either
    remove the leftmost or the rightmost element from the array nums and subtract its value
    from x. Note that this modifies the array for future operations.
    Return the minimum number of operations to reduce x to exactly 0 if it is possible,
    otherwise, return -1.
    Constraints:
        1 <= nums.length <= 10^5
        1 <= nums[i] <= 10^4
        1 <= x <= 10^9
    """

    def minOperations(self, nums: List[int], x: int) -> int:

        n = len(nums)

        # default result value if no operation are found
        res = n + 1

        # start by calculating index i for which sum[:i] > x
        i = running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            if running_sum > x:
                break

        # if the total sum of nums is smaller than x return -1
        if (running_sum < x):
            return -1

        # reduce running sum by last element that made it greater than total
        running_sum -= nums[i]
        i -= 1

        # j is end index (taking values from right until n - j)
        j = -1
        for i in range(i, -2, -1):
            # if current amount of nums to take from right is greater than res, break
            if -j > res:
                break

            # keep increasing amount of nums to take from the array while less than target
            while running_sum < x:
                running_sum += nums[j]
                j -= 1

            # if target is reached, update res if current items taken is less than res
            if running_sum == x:
                items_taken = i - j
                if (items_taken < res):
                    res = items_taken

            # take one less item from left side and repeat
            running_sum -= nums[i]

        # if default value still in res, return -1
        if res == n + 1:
            return -1
        return res
