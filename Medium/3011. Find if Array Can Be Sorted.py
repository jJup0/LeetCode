"""
You are given a 0-indexed array of positive integers nums.

In one operation, you can swap any two adjacent elements if they have the same
number of set bits. You are allowed to do this operation any number of times
(including zero).

Return true if you can sort the array, else return false.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 2^8
"""


class Solution:
    def canSortArray(self, nums: list[int]) -> bool:
        """
        Contiguous subsequences can be permuted freely. Check if the
        index of an element after it has been sorted falls within its
        original bit-count-equal contiguous subsequence.
        Complexity:
            Time: O(n * log(n))
            Space: O(n)
        """

        bit_counts = self._get_bit_counts(nums)

        # sort nums including their original index
        nums_with_idx = sorted(enumerate(nums), key=lambda pair: pair[1])

        bit_count_iter = iter(bit_counts)
        _, start, stop = next(bit_count_iter)
        for i, _ in nums_with_idx:
            if start <= i <= stop:
                # index falls within current interval, all good
                continue

            # index is outside current interval, try next range
            _, start, stop = next(bit_count_iter)
            if not (start <= i <= stop):
                # also not within next interval, cannot be swapped
                # to sorted position
                return False

        # all numbers can be swapped to their sorted position
        return True

    def _get_bit_counts(self, nums: list[int]):
        """Partitions nums by bit count.

        Returns a list `bit_counts` where
            bit_counts[i] = [bit_count, starting_index, ending_index]

        `bit_counts` is n order of how the bit counts appeared in nums,
        terminated by a pseudo entry [-1,-1,-1] which prevents a stop
        iteration occuring when checking if indexes are within the intervals.
        """
        bit_counts: list[list[int]] = [[nums[0].bit_count(), 0, 0]]
        for i, num in enumerate(nums):
            bit_count = num.bit_count()
            if bit_count == bit_counts[-1][0]:
                bit_counts[-1][2] = i
            else:
                bit_counts.append([bit_count, i, i])

        # pseudo bit count, as termination
        bit_counts.append([-1, -1, -1])
        return bit_counts
