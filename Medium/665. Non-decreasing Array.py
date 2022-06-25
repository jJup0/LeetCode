from typing import List


class Solution:
    """
    Given an array nums with n integers, your task is to check if it could become non-decreasing
    by modifying at most one element.
    We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
    such that (0 <= i <= n - 2).
    Constraints:
        n == nums.length
        1 <= n <= 10^4
        -105 <= nums[i] <= 10^5
    """

    def checkPossibility(self, nums: List[int]) -> bool:
        # last val, and val before that
        prev = nums[0]
        prev_prev = -1000000

        # if modifaction has been done already
        modified = False

        # pad nums with greater than maximum constraint
        nums.append(1_000_000)

        for i in range(1, len(nums)-1):

            num = nums[i]
            # if current val less than previous
            if num < prev:
                # if modification has been done already return false
                if modified:
                    nums.pop() # preserve input
                    return False

                # fetch next value
                nxt = nums[i+1]

                # two options to 'fix' array to non-decreasing

                # if previous is bigger than next, have to decrease previous
                # if prev_prev that is smaller than current, then set previous to num
                if prev > nxt and prev_prev <= num:
                    prev = num
                    prev_prev = prev
                # if previous is smaller than next, then set current to previous
                elif prev <= nxt:
                    prev_prev = prev
                # else previous has to be decreased and num has to be increased -> return false
                else:
                    nums.pop() # preserve input
                    return False

                modified = True
            else:
                # update prev and prev_prev
                prev_prev = prev
                prev = num

        nums.pop() # preserve input
        return True
