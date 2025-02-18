"""
You are given a 0-indexed string pattern of length n consisting of the
characters'I' meaning increasing and'D' meaning decreasing.

A 0-indexed string num of length n + 1 is created using the following conditions:
- num consists of the digits'1' to'9', where each digit is used at most once.
- If pattern[i] =='I', then num[i] < num[i + 1].
- If pattern[i] =='D', then num[i] > num[i + 1].

Return the lexicographically smallest possible string num that meets the conditions.

Constraints:
- 1 <= pattern.length <= 8
- pattern consists of only the letters'I' and'D'.
"""


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        At every encounter of "D" increment a counter, at the next encounter
        of an "I" by adding the smallest allowed decreasing sequence.
        Complexity:
            Time: O(n)
            Space: O(n)
        """

        def _extend_descending(nums: list[int], ds_in_a_row: int):
            nums.extend(range(len(nums) + 1 + ds_in_a_row, len(nums), -1))

        # amount of "D"s that where encountered since the last "I"
        ds_in_a_row = 0
        # result as list of numbers
        nums: list[int] = []
        for char in pattern:
            if char == "I":
                _extend_descending(nums, ds_in_a_row)
                ds_in_a_row = 0
            else:
                ds_in_a_row += 1

        _extend_descending(nums, ds_in_a_row)
        return "".join(map(str, nums))
