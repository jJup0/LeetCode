"""
The bitwise AND of an array nums is the bitwise AND of all integers in nums.
- For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
- Also, for nums = [7], the bitwise AND is 7.

You are given an array of positive integers candidates. Evaluate the bitwise
AND of every combination of numbers of candidates. Each number in candidates
may only be used once in each combination.

Return the size of the largest combination of candidates with a bitwise AND
greater than 0.

Constraints:
- 1 <= candidates.length <= 10^5
- 1 <= candidates[i] <= 10^7
"""


class Solution:
    def largestCombination(self, candidates: list[int]) -> int:
        """
        Find the count of the most common set bit.
        Complexity:
            Time: O(n)
            Space: O(n)
        """
        bit_set_count = [0] * 32
        masks = [1 << i for i in range(32)]
        for cand in candidates:
            for bit, mask in enumerate(masks):
                if mask > cand:
                    break
                if cand & mask:
                    bit_set_count[bit] += 1
        return max(bit_set_count)
