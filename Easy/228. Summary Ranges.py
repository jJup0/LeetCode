class Solution:
    """
    You are given a sorted unique integer array nums.

    A range [a,b] is the set of all integers from a to b (inclusive).

    Return the smallest sorted list of ranges that cover all the numbers in the array
    exactly. That is, each element of nums is covered by exactly one of the ranges, and
    there is no integer x such that x is in one of the ranges but not in nums.

    Each range [a,b] in the list should be output as:

    - "a->b" if a != b
    - "a" if a == b

    Constraints:
    - 0 <= nums.length <= 20
    - -2^31 <= nums[i] <= 2^31 - 1
    - All the values of nums are unique.
    - nums is sorted in ascending order.
    """

    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        ret: list[str] = []
        prev = start = nums[0]
        for i in range(1, len(nums)):
            # gap in nums
            if nums[i] - 1 != prev:
                ret.append(str(start) if start == prev else f"{start}->{prev}")
                start = nums[i]

            prev = nums[i]

        ret.append(str(start) if start == prev else f"{start}->{prev}")
        return ret
