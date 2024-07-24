"""
You are given a 0-indexed integer array mapping which represents the mapping
rule of a shuffled decimal system. mapping[i] = j means digit i should be
mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each
occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in
non-decreasing order based on the mapped values of its elements.

Notes:
- Elements with the same mapped values should appear in the same relative order
  as in the input.
- The elements of nums should only be sorted based on their mapped values and
  not be replaced by them.

Constraints:
- mapping.length == 10
- 0 <= mapping[i] <= 9
- All the values of mapping[i] are unique.
- 1 <= nums.length <= 3 * 10^4
- 0 <= nums[i] < 10^9
"""


class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        """
        O(n) / O(n)     time / space complexity
        """
        # create mapping
        mapped_nums: dict[int, int] = {}
        for num in nums:
            if num == 0:
                mapped_nums[0] = mapping[0]
                continue
            remaining_num = num
            mapped_num = 0
            power_10 = 1
            while remaining_num:
                mapped_num += mapping[remaining_num % 10] * power_10
                remaining_num //= 10
                power_10 *= 10
            mapped_nums[num] = mapped_num

        # sort by mapping
        nums.sort(key=lambda num: mapped_nums[num])
        return nums
