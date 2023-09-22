class Solution:
    """
    You are given an integer array nums and an integer x. In one operation, you
    can either remove the leftmost or the rightmost element from the array nums
    and subtract its value from x. Note that this modifies the array for future
    operations.

    Return the minimum number of operations to reduce x to exactly 0 if it is possible,
    otherwise, return -1.

    Constraints:
    - 1 <= nums.length <= 10^5
    - 1 <= nums[i] <= 10^4
    - 1 <= x <= 10^9
    """

    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)

        # default result value if no operation are found
        INF = n + 1
        res = INF

        # start by calculating index i for which sum[:i] > x
        i = running_sum = 0
        for i, num in enumerate(nums):
            running_sum += num
            if running_sum > x:
                break

        # if the total sum of nums is smaller than x return -1
        if running_sum < x:
            return -1

        # j index from which to currently take values from the right side
        j = len(nums) - 1
        # iterate i down to 0
        for i in range(i, -1, -1):
            # assert running_sum >= x

            # take one less item from left side
            running_sum -= nums[i]

            # if current amount of nums to take from right is greater than res, break
            if n - 1 - j > res:
                break

            # keep increasing amount of nums to take from the array while less than target
            while running_sum < x:
                running_sum += nums[j]
                j -= 1

            # if target is reached, update res if current items taken is less than res
            if running_sum == x:
                items_taken = i + (n - 1 - j)
                if items_taken < res:
                    res = items_taken

        # if default value still in res, return -1
        if res == INF:
            return -1
        return res
