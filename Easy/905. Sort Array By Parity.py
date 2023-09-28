from collections import deque


class Solution:
    """
    Given an integer array nums, move all the even integers at the beginning of
    the array followed by all the odd integers.

    Return any array that satisfies this condition.

    Constraints:
    - 1 <= nums.length <= 5000
    - 0 <= nums[i] <= 5000
    """

    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return self.sortArrayByParity_o_n_bucket_branchless(nums)

    def sortArrayByParity_sort(self, nums: list[int]) -> list[int]:
        """
        O(n * log(n)) / O(n)    time / space complexity
        """
        nums.sort(key=lambda x: x & 1)
        return nums

    def sortArrayByParity_o_n_deque(self, nums: list[int]) -> deque[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        res: deque[int] = deque()
        for num in nums:
            if num & 1:
                res.append(num)
            else:
                res.appendleft(num)
        return res

    def sortArrayByParity_o_n_bucket_branchless(self, nums: list[int]) -> list[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        parities: list[list[int]] = [[], []]
        for num in nums:
            parities[num & 1].append(num)
        parities[0].extend(parities[1])
        return parities[0]
